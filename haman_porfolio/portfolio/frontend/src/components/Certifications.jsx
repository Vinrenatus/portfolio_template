import React from "react";
import "../styles/Certifications.css";

const Certifications = ({ certifications }) => {
  return (
    <section className="certifications">
      <div className="container">
        <h2>Professional Certifications</h2>
        <div className="certifications-grid">
          {certifications.map((cert, index) => (
            <div key={index} className="cert-card">
              <div className="cert-icon">
                <i className="fas fa-certificate"></i>
              </div>
              <h3>{cert.name}</h3>
              <p className="cert-issuer">{cert.issuer}</p>
              <div className="cert-details">
                <p><strong>Date:</strong> {cert.date}</p>
                {cert.expires && <p><strong>Expires:</strong> {cert.expires}</p>}
                <p><strong>Credential ID:</strong> {cert.credential_id}</p>
              </div>
              {cert.url ? (
                <a
                  href={cert.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn btn-primary"
                >
                  <i className="fas fa-external-link-alt"></i> View Certificate
                </a>
              ) : (
                <button className="btn btn-primary">View Certificate</button>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Certifications;
