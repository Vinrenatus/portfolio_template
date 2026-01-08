import React, { useState, useEffect } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import "../styles/AdminForm.css";

const EducationAdmin = () => {
  const { token } = useAuth();
  const navigate = useNavigate();
  const [education, setEducation] = useState([]);
  const [newEducation, setNewEducation] = useState({
    institution: "",
    degree: "",
    year: "",
    description: ""
  });
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetchEducationData();
  }, []);

  const fetchEducationData = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/education", {
        headers: {
          "Authorization": `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setEducation(data.education);
      } else {
        setMessage("Failed to load education data");
      }
    } catch (error) {
      setMessage("Error loading education data");
    } finally {
      setLoading(false);
    }
  };

  const handleAddEducation = async (e) => {
    e.preventDefault();
    setSaving(true);
    setMessage("");

    try {
      const response = await fetch("http://localhost:5000/api/education", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify(newEducation),
      });

      if (response.ok) {
        setMessage("Education added successfully!");
        setNewEducation({
          institution: "",
          degree: "",
          year: "",
          description: ""
        });
        fetchEducationData(); // Refresh the list
      } else {
        setMessage("Failed to add education");
      }
    } catch (error) {
      setMessage("Error adding education");
    } finally {
      setSaving(false);
    }
  };

  const handleDeleteEducation = async (index) => {
    if (!window.confirm("Are you sure you want to delete this education?")) {
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/api/education", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ id: index }),
      });

      if (response.ok) {
        setMessage("Education deleted successfully!");
        fetchEducationData(); // Refresh the list
      } else {
        setMessage("Failed to delete education");
      }
    } catch (error) {
      setMessage("Error deleting education");
    }
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="admin-form">
      <h2>Manage Education</h2>
      {message && <div className={`message ${message.includes("successfully") ? "success" : "error"}`}>{message}</div>}
      
      <form onSubmit={handleAddEducation}>
        <div className="form-group">
          <label htmlFor="institution">Institution:</label>
          <input
            type="text"
            id="institution"
            value={newEducation.institution}
            onChange={(e) => setNewEducation({...newEducation, institution: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="degree">Degree:</label>
          <input
            type="text"
            id="degree"
            value={newEducation.degree}
            onChange={(e) => setNewEducation({...newEducation, degree: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="year">Year:</label>
          <input
            type="text"
            id="year"
            value={newEducation.year}
            onChange={(e) => setNewEducation({...newEducation, year: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="description">Description:</label>
          <textarea
            id="description"
            value={newEducation.description}
            onChange={(e) => setNewEducation({...newEducation, description: e.target.value})}
            required
          />
        </div>
        
        <button type="submit" disabled={saving} className="btn btn-primary">
          {saving ? "Saving..." : "Add Education"}
        </button>
      </form>
      
      <div className="item-list">
        <h3>Current Education</h3>
        {education.map((edu, index) => (
          <div key={index} className="item-card">
            <div className="item-card-content">
              <h4>{edu.degree}</h4>
              <p>{edu.institution} - {edu.year}</p>
              <p>{edu.description}</p>
            </div>
            <div className="item-actions">
              <button 
                className="delete-btn"
                onClick={() => handleDeleteEducation(index)}
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

export default EducationAdmin;