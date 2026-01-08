import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { fetchPortfolioData, fetchExperienceData, fetchCertificationsData, fetchTestimonialsData, fetchArticlesData } from "../utils/api";
import Hero from "../components/Hero";
import Skills from "../components/Skills";
import Experience from "../components/Experience";
import Certifications from "../components/Certifications";
import Testimonials from "../components/Testimonials";
import Articles from "../components/Articles";
import "../styles/Home.css";

const Home = () => {
  const [portfolioData, setPortfolioData] = useState(null);
  const [experience, setExperience] = useState([]);
  const [certifications, setCertifications] = useState([]);
  const [testimonials, setTestimonials] = useState([]);
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [portfolio, exp, certs, test, arts] = await Promise.all([
        fetchPortfolioData(),
        fetchExperienceData(),
        fetchCertificationsData(),
        fetchTestimonialsData(),
        fetchArticlesData()
      ]);

      setPortfolioData(portfolio);
      setExperience(exp.experience || []);
      setCertifications(certs.certifications || []);
      setTestimonials(test.testimonials || []);
      setArticles(arts.articles || []);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  // Refresh data when the page becomes visible again (e.g., after returning from admin panel)
  useEffect(() => {
    const handleVisibilityChange = () => {
      if (!document.hidden) {
        fetchData();
      }
    };

    document.addEventListener('visibilitychange', handleVisibilityChange);
    return () => {
      document.removeEventListener('visibilitychange', handleVisibilityChange);
    };
  }, []);

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  if (error) {
    return <div className="loading">Error: {error}</div>;
  }

  if (!portfolioData) {
    return <div className="loading">No data available</div>;
  }

  return (
    <div className="home">
      {/* Hero Section with Sliding Images */}
      <Hero portfolioData={portfolioData} />

      {/* About Section */}
      <section id="about" className="about-section">
        <div className="container">
          <div className="section-header">
            <h2 className="section-title">About Me</h2>
            <div className="section-divider"></div>
          </div>
          <div className="about-content">
            <p className="about-description">{portfolioData.about}</p>
          </div>

          <div className="education-section">
            <h3 className="subsection-title">Education</h3>
            <div className="education-grid">
              {portfolioData.education.map((edu, index) => (
                <div key={index} className="education-card">
                  <div className="education-icon">
                    <i className="fas fa-graduation-cap"></i>
                  </div>
                  <div className="education-details">
                    <h4 className="education-degree">{edu.degree}</h4>
                    <p className="education-institution">{edu.institution} - {edu.year}</p>
                    <p className="education-desc">{edu.description}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Skills Section */}
      <Skills skills={portfolioData.skills} />

      {/* Experience Section */}
      <Experience experience={experience} />

      {/* Certifications Section */}
      <Certifications certifications={certifications} />

      {/* Testimonials Section */}
      <Testimonials testimonials={testimonials} />

      {/* Articles Section */}
      <Articles articles={articles} />
    </div>
  );
};

export default Home;

