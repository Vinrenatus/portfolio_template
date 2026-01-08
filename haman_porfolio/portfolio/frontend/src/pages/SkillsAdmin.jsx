import React, { useState, useEffect } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import "../styles/AdminForm.css";

const SkillsAdmin = () => {
  const { token } = useAuth();
  const navigate = useNavigate();
  const [skills, setSkills] = useState([]);
  const [newSkill, setNewSkill] = useState({
    name: "",
    level: 50
  });
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetchSkillsData();
  }, []);

  const fetchSkillsData = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/skills", {
        headers: {
          "Authorization": `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setSkills(data.skills);
      } else {
        setMessage("Failed to load skills data");
      }
    } catch (error) {
      setMessage("Error loading skills data");
    } finally {
      setLoading(false);
    }
  };

  const handleAddSkill = async (e) => {
    e.preventDefault();
    setSaving(true);
    setMessage("");

    try {
      const response = await fetch("http://localhost:5000/api/skills", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify(newSkill),
      });

      if (response.ok) {
        setMessage("Skill added successfully!");
        setNewSkill({
          name: "",
          level: 50
        });
        fetchSkillsData(); // Refresh the list
      } else {
        setMessage("Failed to add skill");
      }
    } catch (error) {
      setMessage("Error adding skill");
    } finally {
      setSaving(false);
    }
  };

  const handleUpdateSkill = async (index, updatedSkill) => {
    try {
      const response = await fetch("http://localhost:5000/api/skills", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ id: index, ...updatedSkill }),
      });

      if (response.ok) {
        setMessage("Skill updated successfully!");
        fetchSkillsData(); // Refresh the list
      } else {
        setMessage("Failed to update skill");
      }
    } catch (error) {
      setMessage("Error updating skill");
    }
  };

  const handleDeleteSkill = async (index) => {
    if (!window.confirm("Are you sure you want to delete this skill?")) {
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/api/skills", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ id: index }),
      });

      if (response.ok) {
        setMessage("Skill deleted successfully!");
        fetchSkillsData(); // Refresh the list
      } else {
        setMessage("Failed to delete skill");
      }
    } catch (error) {
      setMessage("Error deleting skill");
    }
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="admin-form">
      <h2>Manage Skills</h2>
      {message && <div className={`message ${message.includes("successfully") ? "success" : "error"}`}>{message}</div>}
      
      <form onSubmit={handleAddSkill}>
        <div className="form-group">
          <label htmlFor="skillName">Skill Name:</label>
          <input
            type="text"
            id="skillName"
            value={newSkill.name}
            onChange={(e) => setNewSkill({...newSkill, name: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="skillLevel">Skill Level (0-100):</label>
          <input
            type="number"
            id="skillLevel"
            min="0"
            max="100"
            value={newSkill.level}
            onChange={(e) => setNewSkill({...newSkill, level: parseInt(e.target.value)})}
            required
          />
        </div>
        
        <button type="submit" disabled={saving} className="btn btn-primary">
          {saving ? "Saving..." : "Add Skill"}
        </button>
      </form>
      
      <div className="item-list">
        <h3>Current Skills</h3>
        {skills.map((skill, index) => (
          <div key={index} className="item-card">
            <div className="item-card-content">
              <h4>{skill.name}</h4>
              <p>Level: {skill.level}%</p>
              <div className="skill-bar">
                <div 
                  className="skill-progress" 
                  style={{ width: `${skill.level}%` }}
                ></div>
              </div>
            </div>
            <div className="item-actions">
              <button 
                className="btn btn-secondary"
                onClick={() => handleUpdateSkill(index, { name: skill.name, level: skill.level })}
              >
                Update
              </button>
              <button 
                className="delete-btn"
                onClick={() => handleDeleteSkill(index)}
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

export default SkillsAdmin;