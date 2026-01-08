import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { ThemeProvider } from "./contexts/ThemeContext.jsx";
import { AuthProvider } from "./contexts/AuthContext.jsx";
import ProtectedRoute from "./components/ProtectedRoute.jsx";
import Navbar from "./components/Navbar.jsx";
import Home from "./pages/Home.jsx";
import Projects from "./pages/Projects.jsx";
import Contact from "./pages/Contact.jsx";
import Login from "./pages/Login.jsx";
import Services from "./pages/Services.jsx";
import AdminDashboard from "./pages/AdminDashboard.jsx";
import AboutAdmin from "./pages/AboutAdmin.jsx";
import EducationAdmin from "./pages/EducationAdmin.jsx";
import SkillsAdmin from "./pages/SkillsAdmin.jsx";
import ExperienceAdmin from "./pages/ExperienceAdmin.jsx";
import CertificationsAdmin from "./pages/CertificationsAdmin.jsx";
import ProjectsAdmin from "./pages/ProjectsAdmin.jsx";
import TestimonialsAdmin from "./pages/TestimonialsAdmin.jsx";
import ArticlesAdmin from "./pages/ArticlesAdmin.jsx";
import ResumeAdmin from "./pages/ResumeAdmin.jsx";
import ServicesAdmin from "./pages/ServicesAdmin.jsx";
import ContactMessagesAdmin from "./pages/ContactMessagesAdmin.jsx";
import NewsletterSubscribersAdmin from "./pages/NewsletterSubscribersAdmin.jsx";
import Footer from "./components/Footer.jsx";
import "./styles/App.css";

function App() {
  return (
    <AuthProvider>
      <ThemeProvider>
        <Router>
          <div className="App">
            <Navbar />
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/projects" element={<Projects />} />
              <Route path="/services" element={<Services />} />
              <Route path="/contact" element={<Contact />} />
              <Route path="/login" element={<Login />} />
              <Route
                path="/admin"
                element={
                  <ProtectedRoute>
                    <AdminDashboard />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/about"
                element={
                  <ProtectedRoute>
                    <AboutAdmin />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/education"
                element={
                  <ProtectedRoute>
                    <EducationAdmin />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/skills"
                element={
                  <ProtectedRoute>
                    <SkillsAdmin />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/experience"
                element={
                  <ProtectedRoute>
                    <ExperienceAdmin />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/certifications"
                element={
                  <ProtectedRoute>
                    <CertificationsAdmin />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/projects"
                element={
                  <ProtectedRoute>
                    <ProjectsAdmin />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/testimonials"
                element={
                  <ProtectedRoute>
                    <TestimonialsAdmin />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/articles"
                element={
                  <ProtectedRoute>
                    <ArticlesAdmin />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/resume"
                element={
                  <ProtectedRoute>
                    <ResumeAdmin />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/services"
                element={
                  <ProtectedRoute>
                    <ServicesAdmin />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/messages"
                element={
                  <ProtectedRoute>
                    <ContactMessagesAdmin />
                  </ProtectedRoute>
                }
              />
              <Route
                path="/admin/subscribers"
                element={
                  <ProtectedRoute>
                    <NewsletterSubscribersAdmin />
                  </ProtectedRoute>
                }
              />
            </Routes>
            <Footer />
          </div>
        </Router>
      </ThemeProvider>
    </AuthProvider>
  );
}

export default App;
