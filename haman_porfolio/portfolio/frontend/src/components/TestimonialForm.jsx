import React, { useState } from "react";
import "../styles/TestimonialForm.css";

const TestimonialForm = ({ onSubmission }) => {
  const [testimonial, setTestimonial] = useState({
    name: "",
    title: "",
    company: "",
    content: "",
    avatar: ""
  });
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    try {
      const response = await fetch("http://localhost:5000/api/testimonials", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(testimonial),
      });

      if (response.ok) {
        setMessage("Thank you for your testimonial! It has been submitted for review.");
        setTestimonial({
          name: "",
          title: "",
          company: "",
          content: "",
          avatar: ""
        });
        if (onSubmission) onSubmission();
      } else {
        setMessage("Failed to submit testimonial. Please try again.");
      }
    } catch (error) {
      setMessage("Error submitting testimonial. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="testimonial-form-container">
      <h3>Submit a Testimonial</h3>
      {message && <div className={`message ${message.includes("Thank you") ? "success" : "error"}`}>{message}</div>}
      
      <form onSubmit={handleSubmit} className="testimonial-form">
        <div className="form-group">
          <label htmlFor="testimonialName">Your Name *</label>
          <input
            type="text"
            id="testimonialName"
            value={testimonial.name}
            onChange={(e) => setTestimonial({...testimonial, name: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="testimonialTitle">Your Title</label>
          <input
            type="text"
            id="testimonialTitle"
            value={testimonial.title}
            onChange={(e) => setTestimonial({...testimonial, title: e.target.value})}
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="testimonialCompany">Company</label>
          <input
            type="text"
            id="testimonialCompany"
            value={testimonial.company}
            onChange={(e) => setTestimonial({...testimonial, company: e.target.value})}
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="testimonialContent">Your Testimonial *</label>
          <textarea
            id="testimonialContent"
            value={testimonial.content}
            onChange={(e) => setTestimonial({...testimonial, content: e.target.value})}
            required
            rows="5"
          ></textarea>
        </div>
        
        <div className="form-group">
          <label htmlFor="testimonialAvatar">Avatar URL (optional)</label>
          <input
            type="text"
            id="testimonialAvatar"
            value={testimonial.avatar}
            onChange={(e) => setTestimonial({...testimonial, avatar: e.target.value})}
            placeholder="https://example.com/avatar.jpg"
          />
        </div>
        
        <button type="submit" disabled={loading} className="btn btn-primary">
          {loading ? "Submitting..." : "Submit Testimonial"}
        </button>
      </form>
    </div>
  );
};

export default TestimonialForm;