import os
from app import create_app, db
from app.models import Portfolio, Skill, Education, Experience, Certification, Testimonial, Article, Project, Service, ContactMessage, Resume


def init_db():
    """Initialize the database with all required tables and default data"""
    app = create_app()
    
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if portfolio already exists
        portfolio = Portfolio.query.first()
        if not portfolio:
            # Create default portfolio
            portfolio = Portfolio(
                name="Hamman Muraya",
                title="Senior Software Engineer & DevOps Specialist",
                summary="Highly skilled and dedicated Senior Software Engineer with over 8 years of experience designing, building, and deploying secure, scalable cloud-native systems for fintech and SaaS organisations.",
                about="I am a highly skilled and dedicated Senior Software Engineer with over 8 years of experience designing, building, and deploying secure, scalable cloud-native systems for fintech and SaaS organisations. I am committed to delivering production-grade solutions that meet the highest standards of quality, security, and performance. Since beginning my professional career in software engineering in 2017, I have continuously strived to improve my technical expertise through advanced education, professional certifications, and hands-on experience across diverse technology stacks and cloud platforms. I am highly effective at leading and managing development teams, as well as working independently to prioritise and achieve project targets and business requirements. Throughout my career, I have successfully architected and delivered SOC 2-compliant microservices, optimised database performance for high-throughput systems, and implemented robust CI/CD pipelines using GitOps methodologies. I hold a PhD in Software Engineering from California State University (2019-2022), which enables me to blend academic rigor with practical, production-focused delivery.",
                contact={
                    "email": "muraya.h@yahoo.com",
                    "phone": "+44-747-123-4567",
                    "linkedin": "https://linkedin.com/in/hamman-muraya-8b3744397",
                    "github": "https://github.com/MurayaSoftTouch",
                    "location": "Lincoln, Lincolnshire, England",
                    "website": "https://github.com/MurayaSoftTouch"
                }
            )
            db.session.add(portfolio)
            db.session.commit()
        
        # Add default skills if none exist
        if not Skill.query.first():
            skills = [
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
            ]
            
            for skill_data in skills:
                skill = Skill(
                    name=skill_data["name"],
                    level=skill_data["level"],
                    portfolio_id=portfolio.id
                )
                db.session.add(skill)
        
        # Add default education if none exist
        if not Education.query.first():
            education = [
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
            ]
            
            for edu_data in education:
                edu = Education(
                    institution=edu_data["institution"],
                    degree=edu_data["degree"],
                    year=edu_data["year"],
                    description=edu_data["description"],
                    portfolio_id=portfolio.id
                )
                db.session.add(edu)
        
        # Add default experience if none exist
        if not Experience.query.first():
            experience = [
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
            ]
            
            for exp_data in experience:
                exp = Experience(
                    title=exp_data["title"],
                    company=exp_data["company"],
                    period=exp_data["period"],
                    description=exp_data["description"],
                    portfolio_id=portfolio.id
                )
                db.session.add(exp)
        
        # Add default certifications if none exist
        if not Certification.query.first():
            certifications = [
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
            ]
            
            for cert_data in certifications:
                cert = Certification(
                    name=cert_data["name"],
                    issuer=cert_data["issuer"],
                    date=cert_data["date"],
                    credential_id=cert_data["credential_id"],
                    expires=cert_data["expires"],
                    portfolio_id=portfolio.id
                )
                db.session.add(cert)
        
        # Add default testimonials if none exist
        if not Testimonial.query.first():
            testimonials = [
                {
                    "name": "Dr. Sarah Mitchell",
                    "title": "Professor of Software Engineering",
                    "company": "California State University",
                    "content": "Hamman demonstrated exceptional research abilities and technical expertise during his PhD. His work on scalable microservices architecture has contributed significantly to our research program.",
                    "avatar": "/images/sarah-mitchell.jpg"
                },
                {
                    "name": "James Kariuki",
                    "title": "Head of Engineering",
                    "company": "Power Financial Wellness",
                    "content": "Hamman's cloud architecture skills are outstanding. He designed and implemented a scalable cloud architecture that supported 15,000+ users and processed over $2M in transactions securely.",
                    "avatar": "/images/james-kariuki.jpg"
                },
                {
                    "name": "Michael Chen",
                    "title": "VP Engineering",
                    "company": "Data Annotation",
                    "content": "Hamman led the implementation of a cloud-native microservices architecture that improved system performance by 300% and reduced operational costs by 25%.",
                    "avatar": "/images/michael-chen.jpg"
                }
            ]
            
            for test_data in testimonials:
                test = Testimonial(
                    name=test_data["name"],
                    title=test_data["title"],
                    company=test_data["company"],
                    content=test_data["content"],
                    avatar=test_data["avatar"],
                    portfolio_id=portfolio.id
                )
                db.session.add(test)
        
        # Add default articles if none exist
        if not Article.query.first():
            articles = [
                {
                    "title": "Implementing GitOps with Kubernetes and Flux",
                    "description": "A comprehensive guide to implementing GitOps workflows using Kubernetes and Flux, including practical examples and best practices for production environments.",
                    "date": "October 20, 2023",
                    "url": "https://medium.com/...",
                    "tags": ["Kubernetes", "GitOps", "DevOps"]
                },
                {
                    "title": "Scalable Microservices Architecture for Financial Technology Platforms",
                    "description": "Research paper exploring scalable microservices architecture patterns specifically designed for financial technology platforms, addressing challenges of security, compliance, and performance.",
                    "date": "March 15, 2021",
                    "url": "https://journal.example.com/...",
                    "tags": ["Microservices", "Fintech", "Architecture"]
                }
            ]
            
            for article_data in articles:
                article = Article(
                    title=article_data["title"],
                    description=article_data["description"],
                    date=article_data["date"],
                    url=article_data["url"],
                    tags=article_data["tags"],
                    portfolio_id=portfolio.id
                )
                db.session.add(article)
        
        # Add default projects if none exist
        if not Project.query.first():
            projects = [
                {
                    "title": "Ajali – Real-Time Incident Reporting Platform",
                    "description": "Designed and developed a full-stack emergency response platform using React, Node.js, Flask, and PostgreSQL, featuring real-time geolocation tagging and AWS cloud deployment. This platform enables rapid incident reporting and emergency response coordination, demonstrating technical innovation with real-world social impact.",
                    "technologies": ["React", "Node.js", "Flask", "PostgreSQL", "AWS"],
                    "link": "https://github.com/MurayaSoftTouch",
                    "image": "/images/ajali-platform.jpg",
                    "category": "Full-Stack",
                    "year": "2022"
                },
                {
                    "title": "Sustainable Maasai Legacy E-commerce Platform",
                    "description": "Led end-to-end development of a cultural e-commerce platform using React, Node.js, and Stripe payment integration, enabling Maasai artisans to sell their crafts to global markets. This project generated $15,000 in revenue within the first six months.",
                    "technologies": ["React", "Node.js", "Stripe", "Payment Integration"],
                    "link": "https://github.com/MurayaSoftTouch",
                    "image": "/images/maasai-ecommerce.jpg",
                    "category": "E-commerce",
                    "year": "2021"
                },
                {
                    "title": "CoinBase iOS Cryptocurrency Tracker",
                    "description": "Developed a native iOS application using SwiftUI for real-time cryptocurrency market data visualisation and portfolio tracking. The app features live price updates, portfolio analytics, price alerts, and secure user authentication.",
                    "technologies": ["SwiftUI", "iOS Development", "Real-time Data"],
                    "link": "https://github.com/MurayaSoftTouch",
                    "image": "/images/cryptocurrency-tracker.jpg",
                    "category": "Mobile",
                    "year": "2020"
                },
                {
                    "title": "Science Trivia STEM Learning Application",
                    "description": "Built a gamified STEM learning tool with Flask, PostgreSQL, and JavaScript, featuring dynamic quizzes, leaderboards, progress tracking, and adaptive learning algorithms. This educational platform makes science learning engaging and interactive, with over 1,000 questions across multiple STEM subjects.",
                    "technologies": ["Flask", "PostgreSQL", "JavaScript", "Gamification"],
                    "link": "https://github.com/MurayaSoftTouch",
                    "image": "/images/stem-learning.jpg",
                    "category": "Education",
                    "year": "2020"
                },
                {
                    "title": "Duka Platform RESTful API",
                    "description": "Co-developed a secure RESTful e-commerce backend using Flask, SQLAlchemy, and PostgreSQL, deployed on Render cloud platform with comprehensive API documentation. The platform includes user authentication, product catalog management, shopping cart functionality, and order processing capabilities.",
                    "technologies": ["Flask", "SQLAlchemy", "PostgreSQL", "RESTful API"],
                    "link": "https://github.com/MurayaSoftTouch",
                    "image": "/images/duka-platform.jpg",
                    "category": "Backend",
                    "year": "2020"
                },
                {
                    "title": "3-Tier AWS Infrastructure (Terraform)",
                    "description": "Provisioned a secure, scalable three-tier architecture on AWS using Terraform infrastructure as code, implementing EC2 for application servers, RDS for database management, and S3 for static asset storage. The infrastructure enforces least-privilege IAM policies and network segmentation for enhanced security.",
                    "technologies": ["Terraform", "AWS", "EC2", "RDS", "S3", "IAM"],
                    "link": "https://github.com/MurayaSoftTouch",
                    "image": "/images/aws-infrastructure.jpg",
                    "category": "DevOps",
                    "year": "2019"
                }
            ]
            
            for project_data in projects:
                project = Project(
                    title=project_data["title"],
                    description=project_data["description"],
                    technologies=project_data["technologies"],
                    link=project_data["link"],
                    image=project_data["image"],
                    category=project_data["category"],
                    year=project_data["year"],
                    portfolio_id=portfolio.id
                )
                db.session.add(project)
        
        # Add default services if none exist
        if not Service.query.first():
            services = [
                {
                    "title": "Cloud Architecture & DevOps",
                    "description": "Design and implement scalable cloud-native solutions using AWS, GCP, and Kubernetes. Expert in infrastructure as code with Terraform, CI/CD pipelines, and GitOps methodologies.",
                    "icon": "fas fa-cloud",
                    "features": ["AWS", "GCP", "Kubernetes", "Terraform", "Docker", "CI/CD"]
                },
                {
                    "title": "Full-Stack Development",
                    "description": "End-to-end development of secure, scalable applications using modern technologies like Elixir/Phoenix, React/TypeScript, Python, and Node.js.",
                    "icon": "fas fa-laptop-code",
                    "features": ["Elixir/Phoenix", "React/TypeScript", "Python", "Node.js", "PostgreSQL", "Redis"]
                },
                {
                    "title": "Microservices & API Development",
                    "description": "Architect and develop distributed systems with microservices architecture, secure APIs, and robust inter-service communication patterns.",
                    "icon": "fas fa-project-diagram",
                    "features": ["Microservices", "RESTful APIs", "GraphQL", "gRPC", "Message Queues", "API Gateways"]
                },
                {
                    "title": "Fintech & Security Solutions",
                    "description": "Specialized in financial technology platforms with banking-grade security, compliance (SOC 2, PCI DSS), and high-performance requirements.",
                    "icon": "fas fa-shield-alt",
                    "features": ["SOC 2 Compliance", "PCI DSS", "Authentication", "Encryption", "Security Audits"]
                },
                {
                    "title": "Performance Optimization",
                    "description": "Optimize existing systems for better performance, scalability, and reliability. Database optimization, caching strategies, and system monitoring.",
                    "icon": "fas fa-bolt",
                    "features": ["Redis Caching", "Database Optimization", "Monitoring", "Load Testing", "Profiling"]
                },
                {
                    "title": "Technical Leadership & Mentoring",
                    "description": "Lead development teams, establish coding standards, conduct code reviews, and mentor junior developers to improve overall team performance.",
                    "icon": "fas fa-users",
                    "features": ["Team Leadership", "Code Reviews", "Mentoring", "Agile/Scrum", "Technical Writing"]
                }
            ]
            
            for service_data in services:
                service = Service(
                    title=service_data["title"],
                    description=service_data["description"],
                    icon=service_data["icon"],
                    features=service_data["features"]
                )
                db.session.add(service)
        
        db.session.commit()
        print("Database initialized successfully with default data!")


if __name__ == "__main__":
    init_db()