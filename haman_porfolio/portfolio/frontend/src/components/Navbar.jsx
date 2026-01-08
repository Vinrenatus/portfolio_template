import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useTheme } from "../contexts/ThemeContext";
import { useAuth } from "../contexts/AuthContext";
import "../styles/Navbar.css";

const Navbar = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const { theme, toggleTheme } = useTheme();
  const { isAuthenticated, logout } = useAuth();

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  // Determine theme label safely
  let themeLabel = "Switch to dark mode"; // default
  if (theme && theme === "light") {
    themeLabel = "Switch to dark mode";
  } else if (theme && theme === "dark") {
    themeLabel = "Switch to light mode";
  }

  const handleLogout = () => {
    logout();
  };

  return (
    <nav className={isScrolled ? "navbar scrolled" : "navbar"}>
      <div className="nav-container">
        <Link to="/" className="nav-logo">
          HM
        </Link>

        <div className={isMenuOpen ? "nav-menu active" : "nav-menu"}>
          <Link to="/" className="nav-link" onClick={() => setIsMenuOpen(false)}>
            Home
          </Link>
          <Link to="/projects" className="nav-link" onClick={() => setIsMenuOpen(false)}>
            Projects
          </Link>
          <Link to="/services" className="nav-link" onClick={() => setIsMenuOpen(false)}>
            Services
          </Link>
          <Link to="/contact" className="nav-link" onClick={() => setIsMenuOpen(false)}>
            Contact
          </Link>
        </div>

        <div className="nav-actions">
          {isAuthenticated ? (
            <div className="auth-actions">
              <Link to="/admin" className="admin-dashboard-btn" aria-label="Admin Dashboard">
                <i className="fas fa-tachometer-alt"></i>
              </Link>
              <div className="admin-dropdown">
                <button className="admin-menu-btn" aria-label="Admin Menu">
                  <i className="fas fa-cog"></i>
                </button>
                <div className="admin-dropdown-content">
                  <Link to="/admin/about" className="dropdown-item">
                    <i className="fas fa-user"></i> About
                  </Link>
                  <Link to="/admin/education" className="dropdown-item">
                    <i className="fas fa-graduation-cap"></i> Education
                  </Link>
                  <Link to="/admin/skills" className="dropdown-item">
                    <i className="fas fa-tools"></i> Skills
                  </Link>
                  <Link to="/admin/experience" className="dropdown-item">
                    <i className="fas fa-briefcase"></i> Experience
                  </Link>
                  <Link to="/admin/certifications" className="dropdown-item">
                    <i className="fas fa-certificate"></i> Certifications
                  </Link>
                  <Link to="/admin/projects" className="dropdown-item">
                    <i className="fas fa-project-diagram"></i> Projects
                  </Link>
                  <Link to="/admin/testimonials" className="dropdown-item">
                    <i className="fas fa-comments"></i> Testimonials
                  </Link>
                  <Link to="/admin/articles" className="dropdown-item">
                    <i className="fas fa-newspaper"></i> Articles
                  </Link>
                  <Link to="/admin/services" className="dropdown-item">
                    <i className="fas fa-concierge-bell"></i> Services
                  </Link>
                  <Link to="/admin/messages" className="dropdown-item">
                    <i className="fas fa-envelope"></i> Messages
                  </Link>
                  <Link to="/admin/resume" className="dropdown-item">
                    <i className="fas fa-file-pdf"></i> Resume
                  </Link>
                </div>
              </div>
              <button
                className="logout-btn"
                onClick={handleLogout}
                aria-label="Logout"
              >
                <i className="fas fa-sign-out-alt"></i>
              </button>
            </div>
          ) : (
            <Link to="/login" className="login-btn" aria-label="Login">
              <i className="fas fa-user"></i>
            </Link>
          )}
          <button
            className="theme-toggle"
            onClick={toggleTheme}
            aria-label={themeLabel}
          >
            {theme === "light" ? (
              <i className="fas fa-moon"></i>
            ) : (
              <i className="fas fa-sun"></i>
            )}
          </button>
        </div>

        <div className={isMenuOpen ? "nav-toggle active" : "nav-toggle"} onClick={toggleMenu}>
          <span className="bar"></span>
          <span className="bar"></span>
          <span className="bar"></span>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
