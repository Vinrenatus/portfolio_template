import React, { useState, useEffect } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import "../styles/AdminForm.css";

const ArticlesAdmin = () => {
  const { token } = useAuth();
  const navigate = useNavigate();
  const [articles, setArticles] = useState([]);
  const [newArticle, setNewArticle] = useState({
    title: "",
    description: "",
    date: "",
    url: "",
    tags: ""
  });
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetchArticlesData();
  }, []);

  const fetchArticlesData = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/articles", {
        headers: {
          "Authorization": `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setArticles(data.articles);
      } else {
        setMessage("Failed to load articles data");
      }
    } catch (error) {
      setMessage("Error loading articles data");
    } finally {
      setLoading(false);
    }
  };

  const handleAddArticle = async (e) => {
    e.preventDefault();
    setSaving(true);
    setMessage("");

    try {
      // Convert tags string to array
      const tagsArray = newArticle.tags.split(',').map(t => t.trim());
      
      const response = await fetch("http://localhost:5000/api/articles", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({
          ...newArticle,
          tags: tagsArray
        }),
      });

      if (response.ok) {
        setMessage("Article added successfully!");
        setNewArticle({
          title: "",
          description: "",
          date: "",
          url: "",
          tags: ""
        });
        fetchArticlesData(); // Refresh the list
      } else {
        setMessage("Failed to add article");
      }
    } catch (error) {
      setMessage("Error adding article");
    } finally {
      setSaving(false);
    }
  };

  const handleUpdateArticle = async (index, updatedArticle) => {
    try {
      // Convert tags string to array
      const tagsArray = updatedArticle.tags.split(',').map(t => t.trim());

      const response = await fetch("http://localhost:5000/api/articles", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({
          id: index,
          ...updatedArticle,
          tags: tagsArray
        }),
      });

      if (response.ok) {
        setMessage("Article updated successfully!");
        fetchArticlesData(); // Refresh the list
      } else {
        setMessage("Failed to update article");
      }
    } catch (error) {
      setMessage("Error updating article");
    }
  };

  const handleDeleteArticle = async (index) => {
    if (!window.confirm("Are you sure you want to delete this article?")) {
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/api/articles", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ id: index }),
      });

      if (response.ok) {
        setMessage("Article deleted successfully!");
        fetchArticlesData(); // Refresh the list
      } else {
        setMessage("Failed to delete article");
      }
    } catch (error) {
      setMessage("Error deleting article");
    }
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="admin-form">
      <h2>Manage Articles</h2>
      {message && <div className={`message ${message.includes("successfully") ? "success" : "error"}`}>{message}</div>}
      
      <form onSubmit={handleAddArticle}>
        <div className="form-group">
          <label htmlFor="articleTitle">Title:</label>
          <input
            type="text"
            id="articleTitle"
            value={newArticle.title}
            onChange={(e) => setNewArticle({...newArticle, title: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="articleDescription">Description:</label>
          <textarea
            id="articleDescription"
            value={newArticle.description}
            onChange={(e) => setNewArticle({...newArticle, description: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="articleDate">Date:</label>
          <input
            type="text"
            id="articleDate"
            value={newArticle.date}
            onChange={(e) => setNewArticle({...newArticle, date: e.target.value})}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="articleUrl">URL (for external articles):</label>
          <input
            type="text"
            id="articleUrl"
            value={newArticle.url}
            onChange={(e) => setNewArticle({...newArticle, url: e.target.value})}
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="articleTags">Tags (comma separated):</label>
          <input
            type="text"
            id="articleTags"
            value={newArticle.tags}
            onChange={(e) => setNewArticle({...newArticle, tags: e.target.value})}
          />
        </div>
        
        <button type="submit" disabled={saving} className="btn btn-primary">
          {saving ? "Saving..." : "Add Article"}
        </button>
      </form>
      
      <div className="item-list">
        <h3>Current Articles</h3>
        {articles.map((article, index) => (
          <div key={index} className="item-card">
            <div className="item-card-content">
              <h4>{article.title}</h4>
              <p>{article.description}</p>
              <p><strong>Date:</strong> {article.date}</p>
              {article.url && <p><strong>URL:</strong> <a href={article.url} target="_blank" rel="noopener noreferrer">{article.url}</a></p>}
              <p><strong>Tags:</strong> {article.tags.join(', ')}</p>
            </div>
            <div className="item-actions">
              <button 
                className="btn btn-secondary"
                onClick={() => handleUpdateArticle(index, article)}
              >
                Update
              </button>
              <button 
                className="delete-btn"
                onClick={() => handleDeleteArticle(index)}
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>
      
      <button className="btn btn-secondary" onClick={() => navigate("/admin")}>
        Back to Dashboard
      </button>
    </div>
  );
};

export default ArticlesAdmin;