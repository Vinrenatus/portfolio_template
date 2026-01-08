import React, { useState } from "react";
import { subscribeToNewsletter } from "../utils/api";
import "../styles/Newsletter.css";

const Newsletter = () => {
  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleSubscribe = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    try {
      await subscribeToNewsletter(email);
      setMessage("Thank you for subscribing!");
      setEmail("");
    } catch (error) {
      setMessage("Error subscribing. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="newsletter-section">
      <h3>Stay Updated</h3>
      <p>Subscribe to my newsletter to receive updates on my latest projects, articles, and technical insights.</p>
      <form className="newsletter-form" onSubmit={handleSubscribe}>
        <input
          type="email"
          className="newsletter-input"
          placeholder="Enter your email address to stay updated with my latest projects and insights"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <button type="submit" className="newsletter-btn" disabled={loading}>
          {loading ? "Subscribing..." : "Subscribe"}
        </button>
      </form>
      {message && <div className={`message ${message.includes("Thank you") ? "success" : "error"}`}>{message}</div>}
    </div>
  );
};

export default Newsletter;