import React from "react";
import TestimonialForm from "./TestimonialForm";
import "../styles/Testimonials.css";

const Testimonials = ({ testimonials }) => {
  return (
    <section className="testimonials">
      <div className="container">
        <h2>Testimonials</h2>
        <div className="testimonials-grid">
          {testimonials.map((testimonial, index) => (
            <div key={testimonial.id || index} className="testimonial-card">
              <div className="testimonial-header">
                <img
                  src={testimonial.avatar}
                  alt={testimonial.name}
                  className="testimonial-avatar"
                />
                <div className="testimonial-info">
                  <h3>{testimonial.name}</h3>
                  <p className="testimonial-title">{testimonial.title}</p>
                  <p className="testimonial-company">{testimonial.company}</p>
                </div>
              </div>
              <div className="testimonial-content">
                <p>"{testimonial.content}"</p>
              </div>
              <div className="testimonial-rating">
                <i className="fas fa-star"></i>
                <i className="fas fa-star"></i>
                <i className="fas fa-star"></i>
                <i className="fas fa-star"></i>
                <i className="fas fa-star"></i>
              </div>
            </div>
          ))}
        </div>

        {/* Client testimonial submission form */}
        <div className="testimonial-submission-section">
          <h3>Share Your Experience</h3>
          <p>Have you worked with me? Share your experience and leave a testimonial!</p>
          <TestimonialForm />
        </div>
      </div>
    </section>
  );
};

export default Testimonials;
