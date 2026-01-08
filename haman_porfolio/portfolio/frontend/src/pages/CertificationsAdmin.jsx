import React, { useState, useEffect } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import "../styles/AdminForm.css";

const CertificationsAdmin = () => {
  const { token } = useAuth();
  const navigate = useNavigate();
  const [certifications, setCertifications] = useState([]);
  const [newCertification, setNewCertification] = useState({
    name: "",
    issuer: "",
    date: "",
    credential_id: "",
    expires: "",
    url: ""
  });
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetchCertificationsData();
  }, []);

  const fetchCertificationsData = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/certifications", {
        headers: {
          "Authorization": `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setCertifications(data.certifications);
      } else {
        setMessage("Failed to load certifications data");
      }
    } catch (error) {
      setMessage("Error loading certifications data");
    } finally {
      setLoading(false);
    }
  };

  const handleAddCertification = async (e) => {
    e.preventDefault();
    setSaving(true);
    setMessage("");

    try {
      const response = await fetch("http://localhost:5000/api/certifications", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify(newCertification),
      });

      if (response.ok) {
        setMessage("Certification added successfully!");
        setNewCertification({
          name: "",
          issuer: "",
          date: "",
          credential_id: "",
          expires: ""
        });
        fetchCertificationsData(); // Refresh the list
      } else {
        setMessage("Failed to add certification");
      }
    } catch (error) {
      setMessage("Error adding certification");
    } finally {
      setSaving(false);
    }
  };

  const handleUpdateCertification = async (index, updatedCert) => {
    try {
      const response = await fetch("http://localhost:5000/api/certifications", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ id: index, ...updatedCert }),
      });

      if (response.ok) {
        setMessage("Certification updated successfully!");
        fetchCertificationsData(); // Refresh the list
      } else {
        setMessage("Failed to update certification");
      }
    } catch (error) {
      setMessage("Error updating certification");
    }
  };

  const handleDeleteCertification = async (index) => {
    if (!window.confirm("Are you sure you want to delete this certification?")) {
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/api/certifications", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ id: index }),
      });

      if (response.ok) {
        setMessage("Certification deleted successfully!");
        fetchCertificationsData(); // Refresh the list
      } else {
        setMessage("Failed to delete certification");
      }
    } catch (error) {
      setMessage("Error deleting certification");
    }
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="admin-form">
      <h2>Manage Certifications</h2>
      {message && <div className={`message ${message.includes("successfully") ? "success" : "error"}`}>{message}</div>}
      
      <form onSubmit={handleAddCertification}>
        <div className="form-group">
          <label htmlFor="certName">Name:</label>
          <input
            type="text"
            id="certName"
            value={newCertification.name}
            onChange={(e) => setNewCertification({...newCertification, name: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="certIssuer">Issuer:</label>
          <input
            type="text"
            id="certIssuer"
            value={newCertification.issuer}
            onChange={(e) => setNewCertification({...newCertification, issuer: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="certDate">Date:</label>
          <input
            type="text"
            id="certDate"
            value={newCertification.date}
            onChange={(e) => setNewCertification({...newCertification, date: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="certId">Credential ID:</label>
          <input
            type="text"
            id="certId"
            value={newCertification.credential_id}
            onChange={(e) => setNewCertification({...newCertification, credential_id: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="certExpires">Expires:</label>
          <input
            type="text"
            id="certExpires"
            value={newCertification.expires}
            onChange={(e) => setNewCertification({...newCertification, expires: e.target.value})}
          />
        </div>

        <div className="form-group">
          <label htmlFor="certUrl">Certificate URL (optional):</label>
          <input
            type="url"
            id="certUrl"
            value={newCertification.url}
            onChange={(e) => setNewCertification({...newCertification, url: e.target.value})}
            placeholder="https://example.com/certificate-link"
          />
        </div>

        <button type="submit" disabled={saving} className="btn btn-primary">
          {saving ? "Saving..." : "Add Certification"}
        </button>
      </form>
      
      <div className="item-list">
        <h3>Current Certifications</h3>
        {certifications.map((cert, index) => (
          <div key={index} className="item-card">
            <div className="item-card-content">
              <h4>{cert.name}</h4>
              <p><strong>Issuer:</strong> {cert.issuer}</p>
              <p><strong>Date:</strong> {cert.date}</p>
              <p><strong>Credential ID:</strong> {cert.credential_id}</p>
              {cert.expires && <p><strong>Expires:</strong> {cert.expires}</p>}
              {cert.url && (
                <p>
                  <strong>URL:</strong>
                  <a href={cert.url} target="_blank" rel="noopener noreferrer" className="cert-link">
                    {cert.url}
                  </a>
                </p>
              )}
            </div>
            <div className="item-actions">
              <button 
                className="btn btn-secondary"
                onClick={() => handleUpdateCertification(index, cert)}
              >
                Update
              </button>
              <button 
                className="delete-btn"
                onClick={() => handleDeleteCertification(index)}
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

export default CertificationsAdmin;