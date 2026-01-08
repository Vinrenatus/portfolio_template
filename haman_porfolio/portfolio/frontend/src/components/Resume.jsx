import React from "react";
import "../styles/Resume.css";

const Resume = () => {
  const handleDownload = () => {
    // In a real application, this would download the actual resume file
    // For now, we'll create a simple PDF download using the CV file we already have
    const link = document.createElement("a");
    link.href = "/Hamman_Muraya_DAVIS_STYLE_CV.pdf";
    link.download = "Hamman_Muraya_Resume.pdf";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <button className="resume-btn" onClick={handleDownload}>
      <i className="fas fa-download"></i> Download Resume
    </button>
  );
};

export default Resume;