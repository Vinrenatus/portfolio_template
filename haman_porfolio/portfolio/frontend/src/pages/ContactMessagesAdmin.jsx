import React, { useState, useEffect } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import "../styles/AdminForm.css";

const ContactMessagesAdmin = () => {
  const { token } = useAuth();
  const navigate = useNavigate();
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetchMessagesData();
  }, []);

  const fetchMessagesData = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/contact-messages", {
        headers: {
          "Authorization": `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setMessages(data.messages || []);
      } else {
        setMessage("Failed to load contact messages");
      }
    } catch (error) {
      setMessage("Error loading contact messages");
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteMessage = async (id) => {
    if (!window.confirm("Are you sure you want to delete this message?")) {
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/api/contact-messages", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ id }),
      });

      if (response.ok) {
        setMessage("Message deleted successfully!");
        fetchMessagesData(); // Refresh the list
      } else {
        setMessage("Failed to delete message");
      }
    } catch (error) {
      setMessage("Error deleting message");
    }
  };

  if (loading) {
    return <div className="loading">Loading messages...</div>;
  }

  return (
    <div className="admin-form">
      <h2>Contact Messages Dashboard</h2>
      {message && <div className={`message ${message.includes("successfully") ? "success" : "error"}`}>{message}</div>}
      
      <div className="item-list">
        <h3>All Contact Messages</h3>
        {messages.length > 0 ? (
          messages.map((msg, index) => (
            <div key={msg.id || index} className="item-card">
              <div className="item-card-content">
                <h4>{msg.subject || "No Subject"}</h4>
                <p><strong>Name:</strong> {msg.name}</p>
                <p><strong>Email:</strong> {msg.email}</p>
                <p><strong>Date:</strong> {msg.created_at ? new Date(msg.created_at).toLocaleString() : "Unknown"}</p>
                <p><strong>Message:</strong></p>
                <p>{msg.message}</p>
              </div>
              <div className="item-actions">
                <button 
                  className="delete-btn"
                  onClick={() => handleDeleteMessage(msg.id || index)}
                >
                  Delete
                </button>
              </div>
            </div>
          ))
        ) : (
          <p>No contact messages received yet.</p>
        )}
      </div>
      
      <button className="btn btn-secondary" onClick={() => navigate("/admin")}>
        Back to Dashboard
      </button>
    </div>
  );
};

export default ContactMessagesAdmin;