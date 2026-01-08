import React, { useState, useEffect } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import "../styles/AdminForm.css";

const ExperienceAdmin = () => {
  const { token } = useAuth();
  const navigate = useNavigate();
  const [experience, setExperience] = useState([]);
  const [newExperience, setNewExperience] = useState({
    title: "",
    company: "",
    period: "",
    description: ""
  });
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetchExperienceData();
  }, []);

  const fetchExperienceData = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/experience", {
        headers: {
          "Authorization": `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setExperience(data.experience);
      } else {
        setMessage("Failed to load experience data");
      }
    } catch (error) {
      setMessage("Error loading experience data");
    } finally {
      setLoading(false);
    }
  };

  const handleAddExperience = async (e) => {
    e.preventDefault();
    setSaving(true);
    setMessage("");

    try {
      const response = await fetch("http://localhost:5000/api/experience", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify(newExperience),
      });

      if (response.ok) {
        setMessage("Experience added successfully!");
        setNewExperience({
          title: "",
          company: "",
          period: "",
          description: ""
        });
        fetchExperienceData(); // Refresh the list
      } else {
        setMessage("Failed to add experience");
      }
    } catch (error) {
      setMessage("Error adding experience");
    } finally {
      setSaving(false);
    }
  };

  const handleUpdateExperience = async (index, updatedExp) => {
    try {
      const response = await fetch("http://localhost:5000/api/experience", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ id: index, ...updatedExp }),
      });

      if (response.ok) {
        setMessage("Experience updated successfully!");
        fetchExperienceData(); // Refresh the list
      } else {
        setMessage("Failed to update experience");
      }
    } catch (error) {
      setMessage("Error updating experience");
    }
  };

  const handleDeleteExperience = async (index) => {
    if (!window.confirm("Are you sure you want to delete this experience?")) {
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/api/experience", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ id: index }),
      });

      if (response.ok) {
        setMessage("Experience deleted successfully!");
        fetchExperienceData(); // Refresh the list
      } else {
        setMessage("Failed to delete experience");
      }
    } catch (error) {
      setMessage("Error deleting experience");
    }
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="admin-form">
      <h2>Manage Work Experience</h2>
      {message && <div className={`message ${message.includes("successfully") ? "success" : "error"}`}>{message}</div>}
      
      <form onSubmit={handleAddExperience}>
        <div className="form-group">
          <label htmlFor="expTitle">Title:</label>
          <input
            type="text"
            id="expTitle"
            value={newExperience.title}
            onChange={(e) => setNewExperience({...newExperience, title: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="expCompany">Company:</label>
          <input
            type="text"
            id="expCompany"
            value={newExperience.company}
            onChange={(e) => setNewExperience({...newExperience, company: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="expPeriod">Period:</label>
          <input
            type="text"
            id="expPeriod"
            value={newExperience.period}
            onChange={(e) => setNewExperience({...newExperience, period: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="expDescription">Description:</label>
          <textarea
            id="expDescription"
            value={newExperience.description}
            onChange={(e) => setNewExperience({...newExperience, description: e.target.value})}
            required
          />
        </div>
        
        <button type="submit" disabled={saving} className="btn btn-primary">
          {saving ? "Saving..." : "Add Experience"}
        </button>
      </form>
      
      <div className="item-list">
        <h3>Current Work Experience</h3>
        {experience.map((exp, index) => (
          <div key={index} className="item-card">
            <div className="item-card-content">
              <h4>{exp.title}</h4>
              <p><strong>{exp.company}</strong> - {exp.period}</p>
              <p>{exp.description}</p>
            </div>
            <div className="item-actions">
              <button 
                className="btn btn-secondary"
                onClick={() => handleUpdateExperience(index, exp)}
              >
                Update
              </button>
              <button 
                className="delete-btn"
                onClick={() => handleDeleteExperience(index)}
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

export default ExperienceAdmin;