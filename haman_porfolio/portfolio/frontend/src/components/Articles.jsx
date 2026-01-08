import React from "react";
import "../styles/Articles.css";

const Articles = ({ articles }) => {
  return (
    <section className="articles">
      <div className="container">
        <h2>Articles & Publications</h2>
        <div className="articles-grid">
          {articles.map((article, index) => (
            <div key={article.id || index} className="article-card">
              <div className="article-content">
                <div className="article-tags">
                  {article.tags?.map((tag, tagIndex) => (
                    <span key={tagIndex} className="tag">{tag}</span>
                  )) || []}
                </div>
                <h3>{article.title}</h3>
                <p>{article.description}</p>
                <div className="article-meta">
                  <span className="article-date">{article.date}</span>
                  <a href={article.url} target="_blank" rel="noopener noreferrer" className="read-more">
                    Read More <i className="fas fa-arrow-right"></i>
                  </a>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Articles;
