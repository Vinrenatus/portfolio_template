import json
import os
from datetime import datetime


# Data file path
DATA_FILE = 'data/portfolio_data.json'


def load_data():
    """Load data from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        # Return default data if file doesn't exist
        return get_default_data()


def save_data(data):
    """Save data to JSON file"""
    # Create data directory if it doesn't exist
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def get_default_data():
    """Return default portfolio data"""
    return {
        "name": "Hamman Muraya",
        "title": "Senior Software Engineer & DevOps Specialist",
        "summary": "Highly skilled and dedicated Senior Software Engineer with over 8 years of experience designing, building, and deploying secure, scalable cloud-native systems for fintech and SaaS organisations.",
        "about": "I am a highly skilled and dedicated Senior Software Engineer with over 8 years of experience designing, building, and deploying secure, scalable cloud-native systems for fintech and SaaS organisations. I am committed to delivering production-grade solutions that meet the highest standards of quality, security, and performance. Since beginning my professional career in software engineering in 2017, I have continuously strived to improve my technical expertise through advanced education, professional certifications, and hands-on experience across diverse technology stacks and cloud platforms. I am highly effective at leading and managing development teams, as well as working independently to prioritise and achieve project targets and business requirements. Throughout my career, I have successfully architected and delivered SOC 2-compliant microservices, optimised database performance for high-throughput systems, and implemented robust CI/CD pipelines using GitOps methodologies. I hold a PhD in Software Engineering from California State University (2019-2022), which enables me to blend academic rigor with practical, production-focused delivery.",
        "skills": [
            {"name": "Elixir/Phoenix", "level": 95},
            {"name": "Python", "level": 90},
            {"name": "React/TypeScript", "level": 85},
            {"name": "Node.js/Express", "level": 80},
            {"name": "Go", "level": 70},
            {"name": "PostgreSQL", "level": 90},
            {"name": "Redis", "level": 85},
            {"name": "MongoDB", "level": 80},
            {"name": "AWS", "level": 95},
            {"name": "GCP", "level": 90},
            {"name": "Terraform", "level": 85},
            {"name": "Kubernetes", "level": 90},
            {"name": "Docker", "level": 85},
            {"name": "GraphQL", "level": 80},
            {"name": "Microservices Architecture", "level": 90}
        ],
        "education": [
            {
                "institution": "California State University, California, USA",
                "degree": "PhD in Software Engineering",
                "year": "2019-2022",
                "description": "Thesis: 'Scalable Microservices Architecture for Financial Technology Platforms'"
            },
            {
                "institution": "Lincoln University, Lincoln, UK",
                "degree": "MSc in Software Engineering",
                "year": "2015-2017",
                "description": "Classification: Merit"
            },
            {
                "institution": "University of Nairobi, Nairobi, Kenya",
                "degree": "BSc in Applied Computer Science",
                "year": "2010-2014",
                "description": "Classification: Second Class Honours (Upper Division), GPA: 3.7/4.0"
            }
        ],
        "experience": [
            {
                "title": "Senior Software Engineer",
                "company": "Data Annotation",
                "period": "07/2023 – 07/2025",
                "description": "Architected and maintained highly scalable Elixir microservices running on Google Kubernetes Engine (GKE) using Terraform for infrastructure provisioning. Built SOC 2-compliant systems capable of handling 5,000+ requests per minute with sub-200ms latency."
            },
            {
                "title": "Senior Backend Engineer",
                "company": "Standard Chartered Bank",
                "period": "12/2022 – 06/2023",
                "description": "Optimised existing Elixir and Python services by implementing Redis caching strategies and improving database query performance. Improved system responsiveness by 35%."
            },
            {
                "title": "Senior Backend Engineer",
                "company": "Power Financial Wellness",
                "period": "07/2021 – 11/2022",
                "description": "Designed and implemented a distributed fintech platform on Google Cloud Platform serving 15,000+ users across East Africa."
            }
        ],
        "certifications": [
            {
                "name": "AWS Certified Solutions Architect – Associate",
                "issuer": "Amazon Web Services",
                "date": "January 2022",
                "credential_id": "AWS-SAA-2022-HM001",
                "expires": "January 2025"
            },
            {
                "name": "Certified Kubernetes Administrator (CKA)",
                "issuer": "Cloud Native Computing Foundation",
                "date": "March 2023",
                "credential_id": "CKA-2023-HM002",
                "expires": "March 2026"
            },
            {
                "name": "AWS Certified Cloud Practitioner",
                "issuer": "Amazon Web Services",
                "date": "July 2024",
                "credential_id": "AWS-CCP-2024-HM003",
                "expires": "July 2027"
            }
        ],
        "testimonials": [
            {
                "id": 1,
                "name": "Dr. Sarah Mitchell",
                "title": "Professor of Software Engineering",
                "company": "California State University",
                "content": "Hamman demonstrated exceptional research abilities and technical expertise during his PhD. His work on scalable microservices architecture has contributed significantly to our research program.",
                "avatar": "/images/sarah-mitchell.jpg"
            },
            {
                "id": 2,
                "name": "James Kariuki",
                "title": "Head of Engineering",
                "company": "Power Financial Wellness",
                "content": "Hamman's cloud architecture skills are outstanding. He designed and implemented a scalable cloud architecture that supported 15,000+ users and processed over $2M in transactions securely.",
                "avatar": "/images/james-kariuki.jpg"
            },
            {
                "id": 3,
                "name": "Michael Chen",
                "title": "VP Engineering",
                "company": "Data Annotation",
                "content": "Hamman led the implementation of a cloud-native microservices architecture that improved system performance by 300% and reduced operational costs by 25%.",
                "avatar": "/images/michael-chen.jpg"
            }
        ],
        "articles": [
            {
                "id": 1,
                "title": "Implementing GitOps with Kubernetes and Flux",
                "description": "A comprehensive guide to implementing GitOps workflows using Kubernetes and Flux, including practical examples and best practices for production environments.",
                "date": "October 20, 2023",
                "url": "https://medium.com/...",
                "tags": ["Kubernetes", "GitOps", "DevOps"]
            },
            {
                "id": 2,
                "title": "Scalable Microservices Architecture for Financial Technology Platforms",
                "description": "Research paper exploring scalable microservices architecture patterns specifically designed for financial technology platforms, addressing challenges of security, compliance, and performance.",
                "date": "March 15, 2021",
                "url": "https://journal.example.com/...",
                "tags": ["Microservices", "Fintech", "Architecture"]
            }
        ],
        "contact": {
            "name": "HAMMAN MURAYA",
            "title": "Senior Software Engineer",
            "email": "hamanmuraya009@gmail.com",
            "phone": "+12533784293",
            "linkedin": "www.linkedin.com/in/haman-softwaredev/",
            "github": "github.com/MurayaSoftTouch",
            "location": "Seattle, Washington, United States",
            "website": "github.com/MurayaSoftTouch"
        }
    }


def get_portfolio_data():
    """Get portfolio information"""
    data = load_data()
    return {
        "name": data["name"],
        "title": data["title"],
        "summary": data["summary"],
        "about": data["about"],
        "skills": data["skills"],
        "education": data["education"],
        "experience": data["experience"],
        "certifications": data["certifications"],
        "testimonials": data["testimonials"],
        "articles": data["articles"],
        "contact": data["contact"]
    }


def update_portfolio_data(update_data):
    """Update portfolio information"""
    data = load_data()
    for key, value in update_data.items():
        if key in data:
            data[key] = value
    save_data(data)
    return get_portfolio_data()


def get_projects_data():
    """Get projects information"""
    data = load_data()
    # For now, return default projects - in a real app, this would be separate
    return [
        {
            "id": 1,
            "title": "Ajali – Real-Time Incident Reporting Platform",
            "description": "Designed and developed a full-stack emergency response platform using React, Node.js, Flask, and PostgreSQL, featuring real-time geolocation tagging and AWS cloud deployment. This platform enables rapid incident reporting and emergency response coordination, demonstrating technical innovation with real-world social impact.",
            "technologies": ["React", "Node.js", "Flask", "PostgreSQL", "AWS"],
            "link": "https://github.com/MurayaSoftTouch",
            "image": "/images/ajali-platform.jpg",
            "category": "Full-Stack",
            "year": "2022"
        },
        {
            "id": 2,
            "title": "Sustainable Maasai Legacy E-commerce Platform",
            "description": "Led end-to-end development of a cultural e-commerce platform using React, Node.js, and Stripe payment integration, enabling Maasai artisans to sell their crafts to global markets. This project generated $15,000 in revenue within the first six months.",
            "technologies": ["React", "Node.js", "Stripe", "Payment Integration"],
            "link": "https://github.com/MurayaSoftTouch",
            "image": "/images/maasai-ecommerce.jpg",
            "category": "E-commerce",
            "year": "2021"
        },
        {
            "id": 3,
            "title": "CoinBase iOS Cryptocurrency Tracker",
            "description": "Developed a native iOS application using SwiftUI for real-time cryptocurrency market data visualisation and portfolio tracking. The app features live price updates, portfolio analytics, price alerts, and secure user authentication.",
            "technologies": ["SwiftUI", "iOS Development", "Real-time Data"],
            "link": "https://github.com/MurayaSoftTouch",
            "image": "/images/cryptocurrency-tracker.jpg",
            "category": "Mobile",
            "year": "2020"
        },
        {
            "id": 4,
            "title": "Science Trivia STEM Learning Application",
            "description": "Built a gamified STEM learning tool with Flask, PostgreSQL, and JavaScript, featuring dynamic quizzes, leaderboards, progress tracking, and adaptive learning algorithms. This educational platform makes science learning engaging and interactive, with over 1,000 questions across multiple STEM subjects.",
            "technologies": ["Flask", "PostgreSQL", "JavaScript", "Gamification"],
            "link": "https://github.com/MurayaSoftTouch",
            "image": "/images/stem-learning.jpg",
            "category": "Education",
            "year": "2020"
        },
        {
            "id": 5,
            "title": "Duka Platform RESTful API",
            "description": "Co-developed a secure RESTful e-commerce backend using Flask, SQLAlchemy, and PostgreSQL, deployed on Render cloud platform with comprehensive API documentation. The platform includes user authentication, product catalog management, shopping cart functionality, and order processing capabilities.",
            "technologies": ["Flask", "SQLAlchemy", "PostgreSQL", "RESTful API"],
            "link": "https://github.com/MurayaSoftTouch",
            "image": "/images/duka-platform.jpg",
            "category": "Backend",
            "year": "2020"
        },
        {
            "id": 6,
            "title": "3-Tier AWS Infrastructure (Terraform)",
            "description": "Provisioned a secure, scalable three-tier architecture on AWS using Terraform infrastructure as code, implementing EC2 for application servers, RDS for database management, and S3 for static asset storage. The infrastructure enforces least-privilege IAM policies and network segmentation for enhanced security.",
            "technologies": ["Terraform", "AWS", "EC2", "RDS", "S3", "IAM"],
            "link": "https://github.com/MurayaSoftTouch",
            "image": "/images/aws-infrastructure.jpg",
            "category": "DevOps",
            "year": "2019"
        }
    ]


def get_newsletter_data():
    """Get newsletter information"""
    return {
        "title": "Stay Updated",
        "description": "Subscribe to my newsletter to receive updates on my latest projects, articles, and technical insights.",
        "placeholder": "Enter your email address"
    }


def add_project(project_data):
    """Add a new project (placeholder - in real app would be separate storage)"""
    # In a real application, projects would be stored separately
    # For now, we'll just return the project data
    return project_data


def update_project(project_id, project_data):
    """Update a project (placeholder)"""
    # In a real application, this would update the project in storage
    return project_data


def delete_project(project_id):
    """Delete a project (placeholder)"""
    # In a real application, this would remove the project from storage
    return {"message": f"Project {project_id} deleted successfully"}


def add_experience(exp_data):
    """Add new experience"""
    data = load_data()
    data["experience"].append(exp_data)
    save_data(data)
    return exp_data


def update_experience(index, exp_data):
    """Update experience at index"""
    data = load_data()
    if 0 <= index < len(data["experience"]):
        data["experience"][index] = exp_data
        save_data(data)
        return exp_data
    else:
        raise IndexError("Experience index out of range")


def delete_experience(index):
    """Delete experience at index"""
    data = load_data()
    if 0 <= index < len(data["experience"]):
        data["experience"].pop(index)
        save_data(data)
        return {"message": f"Experience at index {index} deleted successfully"}
    else:
        return {"message": f"Experience at index {index} not found"}


def add_education(edu_data):
    """Add new education"""
    data = load_data()
    data["education"].append(edu_data)
    save_data(data)
    return edu_data


def update_education(index, edu_data):
    """Update education at index"""
    data = load_data()
    if 0 <= index < len(data["education"]):
        data["education"][index] = edu_data
        save_data(data)
        return edu_data
    else:
        raise IndexError("Education index out of range")


def delete_education(index):
    """Delete education at index"""
    data = load_data()
    if 0 <= index < len(data["education"]):
        data["education"].pop(index)
        save_data(data)
        return {"message": f"Education at index {index} deleted successfully"}
    else:
        return {"message": f"Education at index {index} not found"}


def add_skill(skill_data):
    """Add new skill"""
    data = load_data()
    data["skills"].append(skill_data)
    save_data(data)
    return skill_data


def update_skill(index, skill_data):
    """Update skill at index"""
    data = load_data()
    if 0 <= index < len(data["skills"]):
        data["skills"][index] = skill_data
        save_data(data)
        return skill_data
    else:
        raise IndexError("Skill index out of range")


def delete_skill(index):
    """Delete skill at index"""
    data = load_data()
    if 0 <= index < len(data["skills"]):
        data["skills"].pop(index)
        save_data(data)
        return {"message": f"Skill at index {index} deleted successfully"}
    else:
        return {"message": f"Skill at index {index} not found"}


def add_certification(cert_data):
    """Add new certification"""
    data = load_data()
    data["certifications"].append(cert_data)
    save_data(data)
    return cert_data


def update_certification(index, cert_data):
    """Update certification at index"""
    data = load_data()
    if 0 <= index < len(data["certifications"]):
        data["certifications"][index] = cert_data
        save_data(data)
        return cert_data
    else:
        raise IndexError("Certification index out of range")


def delete_certification(index):
    """Delete certification at index"""
    data = load_data()
    if 0 <= index < len(data["certifications"]):
        data["certifications"].pop(index)
        save_data(data)
        return {"message": f"Certification at index {index} deleted successfully"}
    else:
        return {"message": f"Certification at index {index} not found"}


def add_testimonial(test_data):
    """Add new testimonial"""
    data = load_data()
    # Add ID to testimonial
    test_data["id"] = len(data["testimonials"]) + 1
    data["testimonials"].append(test_data)
    save_data(data)
    return test_data


def update_testimonial(index, test_data):
    """Update testimonial at index"""
    data = load_data()
    if 0 <= index < len(data["testimonials"]):
        # Preserve the ID
        test_data["id"] = data["testimonials"][index]["id"]
        data["testimonials"][index] = test_data
        save_data(data)
        return test_data
    else:
        raise IndexError("Testimonial index out of range")


def delete_testimonial(index):
    """Delete testimonial at index"""
    data = load_data()
    if 0 <= index < len(data["testimonials"]):
        data["testimonials"].pop(index)
        save_data(data)
        return {"message": f"Testimonial at index {index} deleted successfully"}
    else:
        return {"message": f"Testimonial at index {index} not found"}


def add_article(article_data):
    """Add new article"""
    data = load_data()
    # Add ID to article
    article_data["id"] = len(data["articles"]) + 1
    data["articles"].append(article_data)
    save_data(data)
    return article_data


def update_article(index, article_data):
    """Update article at index"""
    data = load_data()
    if 0 <= index < len(data["articles"]):
        # Preserve the ID
        article_data["id"] = data["articles"][index]["id"]
        data["articles"][index] = article_data
        save_data(data)
        return article_data
    else:
        raise IndexError("Article index out of range")


def delete_article(index):
    """Delete article at index"""
    data = load_data()
    if 0 <= index < len(data["articles"]):
        data["articles"].pop(index)
        save_data(data)
        return {"message": f"Article at index {index} deleted successfully"}
    else:
        return {"message": f"Article at index {index} not found"}


def add_project(project_data):
    """Add new project"""
    data = load_data()
    # Add ID to project
    project_data["id"] = len(data["projects"]) + 1 if "projects" in data else 1
    if "projects" not in data:
        data["projects"] = []
    data["projects"].append(project_data)
    save_data(data)
    return project_data


def update_project(index, project_data):
    """Update project at index"""
    data = load_data()
    if "projects" in data and 0 <= index < len(data["projects"]):
        # Preserve the ID
        project_data["id"] = data["projects"][index]["id"]
        data["projects"][index] = project_data
        save_data(data)
        return project_data
    else:
        raise IndexError("Project index out of range")


def delete_project(index):
    """Delete project at index"""
    data = load_data()
    if "projects" in data and 0 <= index < len(data["projects"]):
        data["projects"].pop(index)
        save_data(data)
        return {"message": f"Project at index {index} deleted successfully"}
    else:
        return {"message": f"Project at index {index} not found"}


def get_projects_data():
    """Get projects information"""
    data = load_data()
    if "projects" in data:
        return data["projects"]
    else:
        # Return default projects if no projects exist yet
        return [
            {
                "id": 1,
                "title": "Ajali – Real-Time Incident Reporting Platform",
                "description": "Designed and developed a full-stack emergency response platform using React, Node.js, Flask, and PostgreSQL, featuring real-time geolocation tagging and AWS cloud deployment. This platform enables rapid incident reporting and emergency response coordination, demonstrating technical innovation with real-world social impact.",
                "technologies": ["React", "Node.js", "Flask", "PostgreSQL", "AWS"],
                "link": "https://github.com/MurayaSoftTouch",
                "image": "/images/ajali-platform.jpg",
                "category": "Full-Stack",
                "year": "2022"
            },
            {
                "id": 2,
                "title": "Sustainable Maasai Legacy E-commerce Platform",
                "description": "Led end-to-end development of a cultural e-commerce platform using React, Node.js, and Stripe payment integration, enabling Maasai artisans to sell their crafts to global markets. This project generated $15,000 in revenue within the first six months.",
                "technologies": ["React", "Node.js", "Stripe", "Payment Integration"],
                "link": "https://github.com/MurayaSoftTouch",
                "image": "/images/maasai-ecommerce.jpg",
                "category": "E-commerce",
                "year": "2021"
            },
            {
                "id": 3,
                "title": "CoinBase iOS Cryptocurrency Tracker",
                "description": "Developed a native iOS application using SwiftUI for real-time cryptocurrency market data visualisation and portfolio tracking. The app features live price updates, portfolio analytics, price alerts, and secure user authentication.",
                "technologies": ["SwiftUI", "iOS Development", "Real-time Data"],
                "link": "https://github.com/MurayaSoftTouch",
                "image": "/images/cryptocurrency-tracker.jpg",
                "category": "Mobile",
                "year": "2020"
            },
            {
                "id": 4,
                "title": "Science Trivia STEM Learning Application",
                "description": "Built a gamified STEM learning tool with Flask, PostgreSQL, and JavaScript, featuring dynamic quizzes, leaderboards, progress tracking, and adaptive learning algorithms. This educational platform makes science learning engaging and interactive, with over 1,000 questions across multiple STEM subjects.",
                "technologies": ["Flask", "PostgreSQL", "JavaScript", "Gamification"],
                "link": "https://github.com/MurayaSoftTouch",
                "image": "/images/stem-learning.jpg",
                "category": "Education",
                "year": "2020"
            },
            {
                "id": 5,
                "title": "Duka Platform RESTful API",
                "description": "Co-developed a secure RESTful e-commerce backend using Flask, SQLAlchemy, and PostgreSQL, deployed on Render cloud platform with comprehensive API documentation. The platform includes user authentication, product catalog management, shopping cart functionality, and order processing capabilities.",
                "technologies": ["Flask", "SQLAlchemy", "PostgreSQL", "RESTful API"],
                "link": "https://github.com/MurayaSoftTouch",
                "image": "/images/duka-platform.jpg",
                "category": "Backend",
                "year": "2020"
            },
            {
                "id": 6,
                "title": "3-Tier AWS Infrastructure (Terraform)",
                "description": "Provisioned a secure, scalable three-tier architecture on AWS using Terraform infrastructure as code, implementing EC2 for application servers, RDS for database management, and S3 for static asset storage. The infrastructure enforces least-privilege IAM policies and network segmentation for enhanced security.",
                "technologies": ["Terraform", "AWS", "EC2", "RDS", "S3", "IAM"],
                "link": "https://github.com/MurayaSoftTouch",
                "image": "/images/aws-infrastructure.jpg",
                "category": "DevOps",
                "year": "2019"
            }
        ]