import React, { useState } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import "../styles/AdminForm.css";

const ResumeAdmin = () => {
  const { token } = useAuth();
  const navigate = useNavigate();
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState("");
  const [progress, setProgress] = useState(0);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) {
      setMessage("Please select a PDF file to upload");
      return;
    }

    // Check if file is PDF
    if (file.type !== 'application/pdf') {
      setMessage("Please upload a PDF file only");
      return;
    }

    setUploading(true);
    setMessage("");
    setProgress(0);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch("http://localhost:5000/api/resume", {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${token}`,
        },
        body: formData,
      });

      if (response.ok) {
        setMessage("Resume uploaded successfully!");
        setFile(null);
        // Reset form
        document.getElementById('resume-upload-form').reset();
      } else {
        const data = await response.json();
        setMessage(data.message || "Failed to upload resume");
      }
    } catch (error) {
      setMessage("Error uploading resume: " + error.message);
    } finally {
      setUploading(false);
      setProgress(0);
    }
  };

  const handleDownload = () => {
    window.open("http://localhost:5000/api/resume", "_blank");
  };

  return (
    <div className="admin-form">
      <h2>Manage Resume</h2>
      {message && <div className={`message ${message.includes("successfully") ? "success" : "error"}`}>{message}</div>}
      
      <form id="resume-upload-form" onSubmit={handleUpload}>
        <div className="form-group">
          <label htmlFor="resumeFile">Upload Resume (PDF only):</label>
          <input
            type="file"
            id="resumeFile"
            accept=".pdf"
            onChange={handleFileChange}
            required
          />
        </div>
        
        <button type="submit" disabled={uploading} className="btn btn-primary">
          {uploading ? `Uploading... ${progress}%` : "Upload Resume"}
        </button>
      </form>
      
      <div className="item-list">
        <h3>Resume Actions</h3>
        <div className="item-card">
          <div className="item-card-content">
            <h4>Download Current Resume</h4>
            <p>Click the button below to download the currently uploaded resume</p>
          </div>
          <div className="item-actions">
            <button 
              className="btn btn-secondary"
              onClick={handleDownload}
            >
              Download Resume
            </button>
          </div>
        </div>
      </div>
      
      <button className="btn btn-secondary" onClick={() => navigate("/admin")}>
        Back to Dashboard
      </button>
    </div>
  );
};

export default ResumeAdmin;