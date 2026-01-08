import React, { useState, useEffect } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import "../styles/AdminForm.css";

const ProjectsAdmin = () => {
  const { token } = useAuth();
  const navigate = useNavigate();
  const [projects, setProjects] = useState([]);
  const [newProject, setNewProject] = useState({
    title: "",
    description: "",
    technologies: "",
    link: "",
    image: "",
    category: "",
    year: ""
  });
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetchProjectsData();
  }, []);

  const fetchProjectsData = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/projects", {
        headers: {
          "Authorization": `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setProjects(data.projects);
      } else {
        setMessage("Failed to load projects data");
      }
    } catch (error) {
      setMessage("Error loading projects data");
    } finally {
      setLoading(false);
    }
  };

  const handleAddProject = async (e) => {
    e.preventDefault();
    setSaving(true);
    setMessage("");

    try {
      // Convert technologies string to array
      const technologiesArray = newProject.technologies.split(',').map(t => t.trim());
      
      const response = await fetch("http://localhost:5000/api/projects", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({
          ...newProject,
          technologies: technologiesArray
        }),
      });

      if (response.ok) {
        setMessage("Project added successfully!");
        setNewProject({
          title: "",
          description: "",
          technologies: "",
          link: "",
          image: "",
          category: "",
          year: ""
        });
        fetchProjectsData(); // Refresh the list
      } else {
        setMessage("Failed to add project");
      }
    } catch (error) {
      setMessage("Error adding project");
    } finally {
      setSaving(false);
    }
  };

  const handleUpdateProject = async (index, updatedProject) => {
    try {
      // Convert technologies string to array
      const technologiesArray = updatedProject.technologies.split(',').map(t => t.trim());

      const response = await fetch("http://localhost:5000/api/projects", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({
          id: index,
          ...updatedProject,
          technologies: technologiesArray
        }),
      });

      if (response.ok) {
        setMessage("Project updated successfully!");
        fetchProjectsData(); // Refresh the list
      } else {
        setMessage("Failed to update project");
      }
    } catch (error) {
      setMessage("Error updating project");
    }
  };

  const handleDeleteProject = async (index) => {
    if (!window.confirm("Are you sure you want to delete this project?")) {
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/api/projects", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ id: index }),
      });

      if (response.ok) {
        setMessage("Project deleted successfully!");
        fetchProjectsData(); // Refresh the list
      } else {
        setMessage("Failed to delete project");
      }
    } catch (error) {
      setMessage("Error deleting project");
    }
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="admin-form">
      <h2>Manage Projects</h2>
      {message && <div className={`message ${message.includes("successfully") ? "success" : "error"}`}>{message}</div>}
      
      <form onSubmit={handleAddProject}>
        <div className="form-group">
          <label htmlFor="projectTitle">Title:</label>
          <input
            type="text"
            id="projectTitle"
            value={newProject.title}
            onChange={(e) => setNewProject({...newProject, title: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="projectDescription">Description:</label>
          <textarea
            id="projectDescription"
            value={newProject.description}
            onChange={(e) => setNewProject({...newProject, description: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="projectTechnologies">Technologies (comma separated):</label>
          <input
            type="text"
            id="projectTechnologies"
            value={newProject.technologies}
            onChange={(e) => setNewProject({...newProject, technologies: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="projectLink">Link:</label>
          <input
            type="text"
            id="projectLink"
            value={newProject.link}
            onChange={(e) => setNewProject({...newProject, link: e.target.value})}
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="projectImage">Image URL:</label>
          <input
            type="text"
            id="projectImage"
            value={newProject.image}
            onChange={(e) => setNewProject({...newProject, image: e.target.value})}
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="projectCategory">Category:</label>
          <input
            type="text"
            id="projectCategory"
            value={newProject.category}
            onChange={(e) => setNewProject({...newProject, category: e.target.value})}
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="projectYear">Year:</label>
          <input
            type="text"
            id="projectYear"
            value={newProject.year}
            onChange={(e) => setNewProject({...newProject, year: e.target.value})}
          />
        </div>
        
        <button type="submit" disabled={saving} className="btn btn-primary">
          {saving ? "Saving..." : "Add Project"}
        </button>
      </form>
      
      <div className="item-list">
        <h3>Current Projects</h3>
        {projects.map((project, index) => (
          <div key={index} className="item-card">
            <div className="item-card-content">
              <h4>{project.title}</h4>
              <p>{project.description}</p>
              <p><strong>Technologies:</strong> {project.technologies.join(', ')}</p>
              <p><strong>Category:</strong> {project.category} | <strong>Year:</strong> {project.year}</p>
              {project.link && <p><strong>Link:</strong> <a href={project.link} target="_blank" rel="noopener noreferrer">{project.link}</a></p>}
            </div>
            <div className="item-actions">
              <button 
                className="btn btn-secondary"
                onClick={() => handleUpdateProject(index, project)}
              >
                Update
              </button>
              <button 
                className="delete-btn"
                onClick={() => handleDeleteProject(index)}
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

export default ProjectsAdmin;