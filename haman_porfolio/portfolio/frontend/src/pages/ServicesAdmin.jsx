import React, { useState, useEffect } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import "../styles/AdminForm.css";

const ServicesAdmin = () => {
  const { token } = useAuth();
  const navigate = useNavigate();
  const [services, setServices] = useState([]);
  const [newService, setNewService] = useState({
    title: "",
    description: "",
    icon: "",
    features: ""
  });
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetchServicesData();
  }, []);

  const fetchServicesData = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/services", {
        headers: {
          "Authorization": `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setServices(data.services || []);
      } else {
        setMessage("Failed to load services data");
      }
    } catch (error) {
      setMessage("Error loading services data");
    } finally {
      setLoading(false);
    }
  };

  const handleAddService = async (e) => {
    e.preventDefault();
    setSaving(true);
    setMessage("");

    try {
      // Convert features string to array
      const featuresArray = newService.features.split(',').map(f => f.trim());
      
      const response = await fetch("http://localhost:5000/api/services", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({
          ...newService,
          features: featuresArray
        }),
      });

      if (response.ok) {
        setMessage("Service added successfully!");
        setNewService({
          title: "",
          description: "",
          icon: "",
          features: ""
        });
        fetchServicesData(); // Refresh the list
      } else {
        setMessage("Failed to add service");
      }
    } catch (error) {
      setMessage("Error adding service");
    } finally {
      setSaving(false);
    }
  };

  const handleUpdateService = async (id, updatedService) => {
    try {
      // Convert features string to array
      const featuresArray = updatedService.features.split(',').map(f => f.trim());
      
      const response = await fetch("http://localhost:5000/api/services", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ 
          id, 
          ...updatedService,
          features: featuresArray
        }),
      });

      if (response.ok) {
        setMessage("Service updated successfully!");
        fetchServicesData(); // Refresh the list
      } else {
        setMessage("Failed to update service");
      }
    } catch (error) {
      setMessage("Error updating service");
    }
  };

  const handleDeleteService = async (id) => {
    if (!window.confirm("Are you sure you want to delete this service?")) {
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/api/services", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ id }),
      });

      if (response.ok) {
        setMessage("Service deleted successfully!");
        fetchServicesData(); // Refresh the list
      } else {
        setMessage("Failed to delete service");
      }
    } catch (error) {
      setMessage("Error deleting service");
    }
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="admin-form">
      <h2>Manage Services</h2>
      {message && <div className={`message ${message.includes("successfully") ? "success" : "error"}`}>{message}</div>}
      
      <form onSubmit={handleAddService}>
        <div className="form-group">
          <label htmlFor="serviceTitle">Service Title:</label>
          <input
            type="text"
            id="serviceTitle"
            value={newService.title}
            onChange={(e) => setNewService({...newService, title: e.target.value})}
            placeholder="Enter service title (e.g., Cloud Architecture & DevOps)"
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="serviceDescription">Service Description:</label>
          <textarea
            id="serviceDescription"
            value={newService.description}
            onChange={(e) => setNewService({...newService, description: e.target.value})}
            placeholder="Enter service description"
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="serviceIcon">Icon (Font Awesome class):</label>
          <input
            type="text"
            id="serviceIcon"
            value={newService.icon}
            onChange={(e) => setNewService({...newService, icon: e.target.value})}
            placeholder="Enter Font Awesome icon class (e.g., fas fa-cloud)"
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="serviceFeatures">Features (comma separated):</label>
          <input
            type="text"
            id="serviceFeatures"
            value={newService.features}
            onChange={(e) => setNewService({...newService, features: e.target.value})}
            placeholder="Enter features separated by commas (e.g., AWS, GCP, Kubernetes, Terraform)"
          />
        </div>
        
        <button type="submit" disabled={saving} className="btn btn-primary">
          {saving ? "Saving..." : "Add Service"}
        </button>
      </form>
      
      <div className="item-list">
        <h3>Current Services</h3>
        {services.map((service, index) => (
          <div key={service.id || index} className="item-card">
            <div className="item-card-content">
              <h4>{service.title}</h4>
              <p>{service.description}</p>
              <p><strong>Icon:</strong> {service.icon}</p>
              <p><strong>Features:</strong> {Array.isArray(service.features) ? service.features.join(', ') : service.features}</p>
            </div>
            <div className="item-actions">
              <button 
                className="btn btn-secondary"
                onClick={() => handleUpdateService(service.id || index, service)}
              >
                Update
              </button>
              <button 
                className="delete-btn"
                onClick={() => handleDeleteService(service.id || index)}
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

export default ServicesAdmin;