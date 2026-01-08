import React, { useState } from "react";
import { submitContactForm } from "../utils/api";
import Resume from "../components/Resume";
import "../styles/Contact.css";

const Contact = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: ""
  });
  const [status, setStatus] = useState("");
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    setStatus("Sending...");
    setError("");
    
    try {
      await submitContactForm(formData);
      setStatus("Message sent successfully!");
      setFormData({ name: "", email: "", message: "" });
      
      // Reset status after 3 seconds
      setTimeout(() => setStatus(""), 3000);
    } catch (err) {
      setError("Failed to send message. Please try again.");
      setStatus("");
      console.error("Error submitting contact form:", err);
    }
  };

  return (
    <div className="contact">
      <div className="container">
        <h1>Contact Me</h1>
        <p>Feel free to reach out if you want to collaborate with me, or simply have a chat.</p>
        
        <div className="contact-content">
          <div className="contact-info">
            <h2>Get in Touch</h2>
            <p>I'm currently available for freelance work and open to new opportunities.</p>
            
            <div className="contact-details">
              <div className="contact-item">
                <i className="fas fa-envelope"></i>
                <span>{process.env.REACT_APP_CONTACT_EMAIL || "muraya.h@yahoo.com"}</span>
              </div>
              <div className="contact-item">
                <i className="fas fa-phone"></i>
                <span>{process.env.REACT_APP_CONTACT_PHONE || "+44-747-123-4567"}</span>
              </div>
              <div className="contact-item">
                <i className="fas fa-map-marker-alt"></i>
                <span>{process.env.REACT_APP_CONTACT_LOCATION || "Lincoln, Lincolnshire, England"}</span>
              </div>
            </div>
            
            <div className="social-links">
              <a href={process.env.REACT_APP_LINKEDIN_URL || "https://linkedin.com/in/hamman-muraya-8b3744397"} target="_blank" rel="noopener noreferrer">
                <i className="fab fa-linkedin"></i>
              </a>
              <a href={process.env.REACT_APP_GITHUB_URL || "https://github.com/MurayaSoftTouch"} target="_blank" rel="noopener noreferrer">
                <i className="fab fa-github"></i>
              </a>
              <a href={process.env.REACT_APP_TWITTER_URL || "https://twitter.com/hammanmuraya"} target="_blank" rel="noopener noreferrer">
                <i className="fab fa-twitter"></i>
              </a>
            </div>
            
            <div className="resume-section">
              <h3>Download Resume</h3>
              <Resume />
            </div>
          </div>
          
          <form className="contact-form" onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="name">Name</label>
              <input
                type="text"
                id="name"
                name="name"
                value={formData.name}
                onChange={handleChange}
                required
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="message">Message</label>
              <textarea
                id="message"
                name="message"
                rows="5"
                value={formData.message}
                onChange={handleChange}
                required
              ></textarea>
            </div>
            
            <button type="submit" className="btn btn-primary">Send Message</button>
            
            {status && <div className="status-message">{status}</div>}
            {error && <div className="status-message error">{error}</div>}
          </form>
        </div>
      </div>
    </div>
  );
};

export default Contact;