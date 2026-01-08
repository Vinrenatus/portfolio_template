import React, { useState, useEffect } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import "../styles/AdminForm.css";

const TestimonialsAdmin = () => {
  const { token } = useAuth();
  const navigate = useNavigate();
  const [testimonials, setTestimonials] = useState([]);
  const [newTestimonial, setNewTestimonial] = useState({
    name: "",
    title: "",
    company: "",
    content: "",
    avatar: ""
  });
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetchTestimonialsData();
  }, []);

  const fetchTestimonialsData = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/testimonials", {
        headers: {
          "Authorization": `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setTestimonials(data.testimonials);
      } else {
        setMessage("Failed to load testimonials data");
      }
    } catch (error) {
      setMessage("Error loading testimonials data");
    } finally {
      setLoading(false);
    }
  };

  const handleAddTestimonial = async (e) => {
    e.preventDefault();
    setSaving(true);
    setMessage("");

    try {
      const response = await fetch("http://localhost:5000/api/testimonials", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newTestimonial),
      });

      if (response.ok) {
        setMessage("Testimonial submitted successfully! It will be reviewed by admin.");
        setNewTestimonial({
          name: "",
          title: "",
          company: "",
          content: "",
          avatar: ""
        });
        // Don't refresh the list since this is a client submission
      } else {
        setMessage("Failed to submit testimonial");
      }
    } catch (error) {
      setMessage("Error submitting testimonial");
    } finally {
      setSaving(false);
    }
  };

  const handleUpdateTestimonial = async (index, updatedTestimonial) => {
    try {
      const response = await fetch("http://localhost:5000/api/testimonials", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ id: index, ...updatedTestimonial }),
      });

      if (response.ok) {
        setMessage("Testimonial updated successfully!");
        fetchTestimonialsData(); // Refresh the list
      } else {
        setMessage("Failed to update testimonial");
      }
    } catch (error) {
      setMessage("Error updating testimonial");
    }
  };

  const handleDeleteTestimonial = async (index) => {
    if (!window.confirm("Are you sure you want to delete this testimonial?")) {
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/api/testimonials", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ id: index }),
      });

      if (response.ok) {
        setMessage("Testimonial deleted successfully!");
        fetchTestimonialsData(); // Refresh the list
      } else {
        setMessage("Failed to delete testimonial");
      }
    } catch (error) {
      setMessage("Error deleting testimonial");
    }
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="admin-form">
      <h2>Manage Testimonials</h2>
      {message && <div className={`message ${message.includes("successfully") ? "success" : "error"}`}>{message}</div>}
      
      <form onSubmit={handleAddTestimonial}>
        <div className="form-group">
          <label htmlFor="testimonialName">Name:</label>
          <input
            type="text"
            id="testimonialName"
            value={newTestimonial.name}
            onChange={(e) => setNewTestimonial({...newTestimonial, name: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="testimonialTitle">Title:</label>
          <input
            type="text"
            id="testimonialTitle"
            value={newTestimonial.title}
            onChange={(e) => setNewTestimonial({...newTestimonial, title: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="testimonialCompany">Company:</label>
          <input
            type="text"
            id="testimonialCompany"
            value={newTestimonial.company}
            onChange={(e) => setNewTestimonial({...newTestimonial, company: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="testimonialContent">Content:</label>
          <textarea
            id="testimonialContent"
            value={newTestimonial.content}
            onChange={(e) => setNewTestimonial({...newTestimonial, content: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="testimonialAvatar">Avatar URL:</label>
          <input
            type="text"
            id="testimonialAvatar"
            value={newTestimonial.avatar}
            onChange={(e) => setNewTestimonial({...newTestimonial, avatar: e.target.value})}
          />
        </div>
        
        <button type="submit" disabled={saving} className="btn btn-primary">
          {saving ? "Saving..." : "Add Testimonial"}
        </button>
      </form>
      
      <div className="item-list">
        <h3>Current Testimonials</h3>
        {testimonials.map((testimonial, index) => (
          <div key={index} className="item-card">
            <div className="item-card-content">
              <h4>{testimonial.name}</h4>
              <p><strong>{testimonial.title}</strong> at {testimonial.company}</p>
              <p>{testimonial.content}</p>
              {testimonial.avatar && <p><strong>Avatar:</strong> {testimonial.avatar}</p>}
            </div>
            <div className="item-actions">
              <button 
                className="btn btn-secondary"
                onClick={() => handleUpdateTestimonial(index, testimonial)}
              >
                Update
              </button>
              <button 
                className="delete-btn"
                onClick={() => handleDeleteTestimonial(index)}
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>
      
      <button className="btn btn-secondary" onClick={() => navigate("/admin")}>
        Back to Dashboard
      </button>
    </div>
  );
};

export default TestimonialsAdmin;