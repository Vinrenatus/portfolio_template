import React from "react";
import Resume from "./Resume";
import Newsletter from "./Newsletter";
import "../styles/Footer.css";

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-section">
          <h3>Hamman Muraya</h3>
          <p>Senior Software Engineer & DevOps Specialist</p>
          <div className="footer-resume">
            <Resume />
          </div>
        </div>

        <div className="footer-section">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/projects">Projects</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>
        </div>

        <div className="footer-section">
          <h4>Connect</h4>
          <div className="social-links">
            <a href="https://linkedin.com/in/hamman-muraya-8b3744397" target="_blank" rel="noopener noreferrer">
              <i className="fab fa-linkedin"></i>
            </a>
            <a href="https://github.com/MurayaSoftTouch" target="_blank" rel="noopener noreferrer">
              <i className="fab fa-github"></i>
            </a>
            <a href="https://twitter.com/hammanmuraya" target="_blank" rel="noopener noreferrer">
              <i className="fab fa-twitter"></i>
            </a>
            <a href="mailto:muraya.h@yahoo.com">
              <i className="fas fa-envelope"></i>
            </a>
          </div>
        </div>

        <div className="footer-section">
          <Newsletter />
        </div>
      </div>

      <div className="footer-bottom">
        <p>&copy; {new Date().getFullYear()} Hamman Muraya. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;
