import React, { useState, useEffect } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import "../styles/AdminForm.css";

const NewsletterSubscribersAdmin = () => {
  const { token } = useAuth();
  const navigate = useNavigate();
  const [subscribers, setSubscribers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetchSubscribers();
  }, []);

  const fetchSubscribers = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/newsletter", {
        headers: {
          "Authorization": `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setSubscribers(data.subscribers || []);
      } else {
        setMessage("Failed to load subscribers");
      }
    } catch (error) {
      setMessage("Error loading subscribers");
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteSubscriber = async (id) => {
    if (!window.confirm("Are you sure you want to delete this subscriber?")) {
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/api/newsletter", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ id }),
      });

      if (response.ok) {
        setMessage("Subscriber deleted successfully!");
        fetchSubscribers(); // Refresh the list
      } else {
        setMessage("Failed to delete subscriber");
      }
    } catch (error) {
      setMessage("Error deleting subscriber");
    }
  };

  if (loading) {
    return <div className="loading">Loading subscribers...</div>;
  }

  return (
    <div className="admin-form">
      <h2>Newsletter Subscribers</h2>
      {message && <div className={`message ${message.includes("successfully") ? "success" : "error"}`}>{message}</div>}
      
      <div className="item-list">
        <h3>Subscribers ({subscribers.length})</h3>
        {subscribers.length > 0 ? (
          <div className="subscribers-grid">
            {subscribers.map((subscriber) => (
              <div key={subscriber.id} className="item-card">
                <div className="item-card-content">
                  <h4>{subscriber.email}</h4>
                  <p><strong>Subscribed:</strong> {new Date(subscriber.subscribed_at).toLocaleDateString()}</p>
                  <p><strong>Time:</strong> {new Date(subscriber.subscribed_at).toLocaleTimeString()}</p>
                </div>
                <div className="item-actions">
                  <button 
                    className="delete-btn"
                    onClick={() => handleDeleteSubscriber(subscriber.id)}
                  >
                    Remove
                  </button>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <p>No subscribers yet.</p>
        )}
      </div>
      
      <button className="btn btn-secondary" onClick={() => navigate("/admin")}>
        Back to Dashboard
      </button>
    </div>
  );
};

export default NewsletterSubscribersAdmin;