import React from "react";
import { Link } from "react-router-dom";
import "../styles/Hero.css";

const Hero = ({ portfolioData }) => {
  if (!portfolioData) {
    return null;
  }

  return (
    <section className="stationary-hero">
      <div className="stationary-hero-content">
        <h1>{portfolioData.name}</h1>
        <h2>{portfolioData.title}</h2>
        <p>{portfolioData.summary}</p>
        <div className="hero-buttons">
          <Link to="/services" className="btn btn-primary glow-effect">
            <i className="fas fa-cogs mr-2"></i>View Services
          </Link>
          <Link to="/projects" className="btn btn-secondary glow-effect">
            <i className="fas fa-project-diagram mr-2"></i>View Projects
          </Link>
        </div>
      </div>
    </section>
  );
};

export default Hero;