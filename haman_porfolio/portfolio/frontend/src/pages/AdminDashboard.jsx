import React, { useState, useEffect } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import "../styles/AdminDashboard.css";

const AdminDashboard = () => {
  const { isAuthenticated, logout } = useAuth();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!isAuthenticated) {
      navigate("/login");
    } else {
      setLoading(false);
    }
  }, [isAuthenticated, navigate]);

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  const handleLogout = () => {
    logout();
    navigate("/");
  };

  const menuItems = [
    { id: "about", title: "About Me", path: "/admin/about" },
    { id: "education", title: "Education", path: "/admin/education" },
    { id: "skills", title: "Skills", path: "/admin/skills" },
    { id: "experience", title: "Work Experience", path: "/admin/experience" },
    { id: "certifications", title: "Certifications", path: "/admin/certifications" },
    { id: "projects", title: "Projects", path: "/admin/projects" },
    { id: "testimonials", title: "Testimonials", path: "/admin/testimonials" },
    { id: "articles", title: "Articles", path: "/admin/articles" },
    { id: "services", title: "Services", path: "/admin/services" },
    { id: "messages", title: "Contact Messages", path: "/admin/messages" },
    { id: "subscribers", title: "Newsletter Subscribers", path: "/admin/subscribers" },
    { id: "resume", title: "Resume", path: "/admin/resume" },
  ];

  const handleMenuItemClick = (path) => {
    navigate(path);
  };

  return (
    <div className="admin-dashboard">
      <div className="admin-header">
        <h1>Admin Dashboard</h1>
        <button className="logout-btn" onClick={handleLogout}>
          Logout
        </button>
      </div>
      
      <div className="admin-menu">
        <h2>Manage Content</h2>
        <div className="menu-grid">
          {menuItems.map((item) => (
            <div 
              key={item.id} 
              className="menu-item"
              onClick={() => handleMenuItemClick(item.path)}
            >
              <h3>{item.title}</h3>
              <p>Manage {item.title.toLowerCase()}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;