import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { fetchServicesData } from "../utils/api";
import "../styles/Services.css";

const Services = () => {
  const [services, setServices] = useState([]);
  const [currentSlide, setCurrentSlide] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await fetchServicesData();
        setServices(data.services || []);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  // Auto-rotate slides every 8 seconds
  useEffect(() => {
    if (services.length > 0) {
      const interval = setInterval(() => {
        setCurrentSlide((prevSlide) => (prevSlide + 1) % services.length);
      }, 8000);

      return () => clearInterval(interval);
    }
  }, [services.length]);

  const nextSlide = () => {
    setCurrentSlide((prevSlide) => (prevSlide + 1) % services.length);
  };

  const prevSlide = () => {
    setCurrentSlide((prevSlide) => (prevSlide - 1 + services.length) % services.length);
  };

  const goToSlide = (index) => {
    setCurrentSlide(index);
  };

  if (loading) {
    return <div className="loading">Loading services...</div>;
  }

  if (error) {
    return <div className="loading">Error: {error}</div>;
  }

  // Service-related images
  const serviceImages = [
    "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1200&q=80", // Cloud Architecture
    "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1200&q=80", // Full-Stack Development
    "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1200&q=80", // Microservices
    "https://images.unsplash.com/photo-1563014959-7aaa83350985?auto=format&fit=crop&w=1200&q=80", // Fintech Security
    "https://images.unsplash.com/photo-1553877522-43269d4ea984?auto=format&fit=crop&w=1200&q=80", // Performance
    "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=1200&q=80"  // Leadership
  ];

  return (
    <div className="services-page">
      <section className="services-hero">
        <div className="container">
          <h1>Professional Services</h1>
          <p>Explore the professional services I offer to help your business succeed with innovative technology solutions.</p>
        </div>
      </section>

      {/* Services Carousel */}
      <section className="services-carousel">
        <div className="services-carousel-container">
          <div
            className="services-carousel-slide"
            style={{ transform: `translateX(-${currentSlide * 100}%)` }}
          >
            {services.map((service, index) => (
              <div key={service.id || index} className="service-slide-item">
                <div
                  className="service-slide-image"
                  style={{ backgroundImage: `url(${serviceImages[index % serviceImages.length]})` }}
                ></div>
                <div className="service-slide-content">
                  <div className="service-slide-text">
                    <h1>{service.title}</h1>
                    <h2>{service.description}</h2>
                    <div className="service-slide-tech">
                      {service.features?.map((feature, idx) => (
                        <span key={idx} className="service-tech-tag">{feature}</span>
                      ))}
                    </div>
                    <div className="hero-buttons">
                      <Link to="/contact" className="btn btn-primary">Get in Touch</Link>
                      <Link to="/projects" className="btn btn-secondary">View Projects</Link>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Carousel controls */}
          <button className="services-carousel-btn services-prev-btn" onClick={prevSlide}>
            <i className="fas fa-chevron-left"></i>
          </button>
          <button className="services-carousel-btn services-next-btn" onClick={nextSlide}>
            <i className="fas fa-chevron-right"></i>
          </button>

          {/* Slide indicators */}
          <div className="services-carousel-indicators">
            {services.map((_, index) => (
              <button
                key={index}
                className={`services-indicator ${index === currentSlide ? 'active' : ''}`}
                onClick={() => goToSlide(index)}
              ></button>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
};

export default Services;