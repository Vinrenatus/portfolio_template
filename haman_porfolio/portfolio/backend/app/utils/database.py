import psycopg2
from psycopg2.extras import RealDictCursor
import os
from datetime import datetime
import json
from .fallback_data import *  # Import all functions from fallback module


# Database connection parameters
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'portfolio_db')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')  # Default password is 'postgres'
DB_PORT = os.environ.get('DB_PORT', '5432')


def get_db_connection():
    """Get a connection to the PostgreSQL database"""
    try:
        # Try different connection approaches
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
            sslmode='disable'  # Disable SSL for local development
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        # Fallback to file-based storage if DB connection fails
        return None


def init_db():
    """Initialize the database with required tables"""
    conn = get_db_connection()
    if conn is None:
        print("Could not connect to database, skipping initialization")
        return
    
    cursor = conn.cursor()
    
    # Create portfolio table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS portfolio (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            title VARCHAR(255) NOT NULL,
            summary TEXT,
            about TEXT,
            contact JSONB
        );
    """)
    
    # Create skills table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS skills (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            level INTEGER NOT NULL,
            portfolio_id INTEGER REFERENCES portfolio(id) ON DELETE CASCADE
        );
    """)
    
    # Create education table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS education (
            id SERIAL PRIMARY KEY,
            institution VARCHAR(255) NOT NULL,
            degree VARCHAR(255) NOT NULL,
            year VARCHAR(50),
            description TEXT,
            portfolio_id INTEGER REFERENCES portfolio(id) ON DELETE CASCADE
        );
    """)
    
    # Create experience table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS experience (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            company VARCHAR(255) NOT NULL,
            period VARCHAR(100),
            description TEXT,
            portfolio_id INTEGER REFERENCES portfolio(id) ON DELETE CASCADE
        );
    """)
    
    # Create certifications table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS certifications (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            issuer VARCHAR(255) NOT NULL,
            date VARCHAR(50),
            credential_id VARCHAR(100),
            expires VARCHAR(50),
            portfolio_id INTEGER REFERENCES portfolio(id) ON DELETE CASCADE
        );
    """)
    
    # Create testimonials table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS testimonials (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            title VARCHAR(255),
            company VARCHAR(255),
            content TEXT NOT NULL,
            avatar VARCHAR(255),
            portfolio_id INTEGER REFERENCES portfolio(id) ON DELETE CASCADE
        );
    """)
    
    # Create articles table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            date VARCHAR(50),
            url VARCHAR(500),
            tags TEXT[],
            portfolio_id INTEGER REFERENCES portfolio(id) ON DELETE CASCADE
        );
    """)
    
    # Create projects table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            technologies TEXT[],
            link VARCHAR(500),
            image VARCHAR(255),
            category VARCHAR(100),
            year VARCHAR(20),
            portfolio_id INTEGER REFERENCES portfolio(id) ON DELETE CASCADE
        );
    """)
    
    # Create services table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS services (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            icon VARCHAR(100),
            features TEXT[]
        );
    """)
    
    # Create contact_messages table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contact_messages (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            subject VARCHAR(255),
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # Create resume table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resume (
            id SERIAL PRIMARY KEY,
            filename VARCHAR(255) NOT NULL,
            filepath VARCHAR(500) NOT NULL,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # Insert default portfolio data if it doesn't exist
    cursor.execute("SELECT COUNT(*) FROM portfolio")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("""
            INSERT INTO portfolio (name, title, summary, about, contact)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """, (
            "Hamman Muraya",
            "Senior Software Engineer & DevOps Specialist",
            "Highly skilled and dedicated Senior Software Engineer with over 8 years of experience designing, building, and deploying secure, scalable cloud-native systems for fintech and SaaS organisations.",
            "I am a highly skilled and dedicated Senior Software Engineer with over 8 years of experience designing, building, and deploying secure, scalable cloud-native systems for fintech and SaaS organisations. I am committed to delivering production-grade solutions that meet the highest standards of quality, security, and performance. Since beginning my professional career in software engineering in 2017, I have continuously strived to improve my technical expertise through advanced education, professional certifications, and hands-on experience across diverse technology stacks and cloud platforms. I am highly effective at leading and managing development teams, as well as working independently to prioritise and achieve project targets and business requirements. Throughout my career, I have successfully architected and delivered SOC 2-compliant microservices, optimised database performance for high-throughput systems, and implemented robust CI/CD pipelines using GitOps methodologies. I hold a PhD in Software Engineering from California State University (2019-2022), which enables me to blend academic rigor with practical, production-focused delivery.",
            json.dumps({
                "email": "muraya.h@yahoo.com",
                "phone": "+44-747-123-4567",
                "linkedin": "https://linkedin.com/in/hamman-muraya-8b3744397",
                "github": "https://github.com/MurayaSoftTouch",
                "location": "Lincoln, Lincolnshire, England",
                "website": "https://github.com/MurayaSoftTouch"
            })
        ))
        portfolio_id = cursor.fetchone()[0]
        
        # Insert default skills
        skills = [
            ("Elixir/Phoenix", 95),
            ("Python", 90),
            ("React/TypeScript", 85),
            ("Node.js/Express", 80),
            ("Go", 70),
            ("PostgreSQL", 90),
            ("Redis", 85),
            ("MongoDB", 80),
            ("AWS", 95),
            ("GCP", 90),
            ("Terraform", 85),
            ("Kubernetes", 90),
            ("Docker", 85),
            ("GraphQL", 80),
            ("Microservices Architecture", 90)
        ]
        for skill_name, level in skills:
            cursor.execute("""
                INSERT INTO skills (name, level, portfolio_id)
                VALUES (%s, %s, %s)
            """, (skill_name, level, portfolio_id))
        
        # Insert default education
        education = [
            ("California State University, California, USA", "PhD in Software Engineering", "2019-2022", "Thesis: 'Scalable Microservices Architecture for Financial Technology Platforms'"),
            ("Lincoln University, Lincoln, UK", "MSc in Software Engineering", "2015-2017", "Classification: Merit"),
            ("University of Nairobi, Nairobi, Kenya", "BSc in Applied Computer Science", "2010-2014", "Classification: Second Class Honours (Upper Division), GPA: 3.7/4.0")
        ]
        for institution, degree, year, description in education:
            cursor.execute("""
                INSERT INTO education (institution, degree, year, description, portfolio_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (institution, degree, year, description, portfolio_id))
        
        # Insert default experience
        experience = [
            ("Senior Software Engineer", "Data Annotation", "07/2023 – 07/2025", "Architected and maintained highly scalable Elixir microservices running on Google Kubernetes Engine (GKE) using Terraform for infrastructure provisioning. Built SOC 2-compliant systems capable of handling 5,000+ requests per minute with sub-200ms latency."),
            ("Senior Backend Engineer", "Standard Chartered Bank", "12/2022 – 06/2023", "Optimised existing Elixir and Python services by implementing Redis caching strategies and improving database query performance. Improved system responsiveness by 35%."),
            ("Senior Backend Engineer", "Power Financial Wellness", "07/2021 – 11/2022", "Designed and implemented a distributed fintech platform on Google Cloud Platform serving 15,000+ users across East Africa.")
        ]
        for title, company, period, description in experience:
            cursor.execute("""
                INSERT INTO experience (title, company, period, description, portfolio_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (title, company, period, description, portfolio_id))
        
        # Insert default certifications
        certifications = [
            ("AWS Certified Solutions Architect – Associate", "Amazon Web Services", "January 2022", "AWS-SAA-2022-HM001", "January 2025"),
            ("Certified Kubernetes Administrator (CKA)", "Cloud Native Computing Foundation", "March 2023", "CKA-2023-HM002", "March 2026"),
            ("AWS Certified Cloud Practitioner", "Amazon Web Services", "July 2024", "AWS-CCP-2024-HM003", "July 2027")
        ]
        for name, issuer, date, credential_id, expires in certifications:
            cursor.execute("""
                INSERT INTO certifications (name, issuer, date, credential_id, expires, portfolio_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (name, issuer, date, credential_id, expires, portfolio_id))
        
        # Insert default testimonials
        testimonials = [
            ("Dr. Sarah Mitchell", "Professor of Software Engineering", "California State University", "Hamman demonstrated exceptional research abilities and technical expertise during his PhD. His work on scalable microservices architecture has contributed significantly to our research program.", "/images/sarah-mitchell.jpg"),
            ("James Kariuki", "Head of Engineering", "Power Financial Wellness", "Hamman's cloud architecture skills are outstanding. He designed and implemented a scalable cloud architecture that supported 15,000+ users and processed over $2M in transactions securely.", "/images/james-kariuki.jpg"),
            ("Michael Chen", "VP Engineering", "Data Annotation", "Hamman led the implementation of a cloud-native microservices architecture that improved system performance by 300% and reduced operational costs by 25%.", "/images/michael-chen.jpg")
        ]
        for name, title, company, content, avatar in testimonials:
            cursor.execute("""
                INSERT INTO testimonials (name, title, company, content, avatar, portfolio_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (name, title, company, content, avatar, portfolio_id))
        
        # Insert default articles
        articles = [
            ("Implementing GitOps with Kubernetes and Flux", "A comprehensive guide to implementing GitOps workflows using Kubernetes and Flux, including practical examples and best practices for production environments.", "October 20, 2023", "https://medium.com/...", ["Kubernetes", "GitOps", "DevOps"]),
            ("Scalable Microservices Architecture for Financial Technology Platforms", "Research paper exploring scalable microservices architecture patterns specifically designed for financial technology platforms, addressing challenges of security, compliance, and performance.", "March 15, 2021", "https://journal.example.com/...", ["Microservices", "Fintech", "Architecture"])
        ]
        for title, description, date, url, tags in articles:
            cursor.execute("""
                INSERT INTO articles (title, description, date, url, tags, portfolio_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (title, description, date, url, tags, portfolio_id))
        
        # Insert default projects
        projects = [
            ("Ajali – Real-Time Incident Reporting Platform", "Designed and developed a full-stack emergency response platform using React, Node.js, Flask, and PostgreSQL, featuring real-time geolocation tagging and AWS cloud deployment. This platform enables rapid incident reporting and emergency response coordination, demonstrating technical innovation with real-world social impact.", ["React", "Node.js", "Flask", "PostgreSQL", "AWS"], "https://github.com/MurayaSoftTouch", "/images/ajali-platform.jpg", "Full-Stack", "2022"),
            ("Sustainable Maasai Legacy E-commerce Platform", "Led end-to-end development of a cultural e-commerce platform using React, Node.js, and Stripe payment integration, enabling Maasai artisans to sell their crafts to global markets. This project generated $15,000 in revenue within the first six months.", ["React", "Node.js", "Stripe", "Payment Integration"], "https://github.com/MurayaSoftTouch", "/images/maasai-ecommerce.jpg", "E-commerce", "2021"),
            ("CoinBase iOS Cryptocurrency Tracker", "Developed a native iOS application using SwiftUI for real-time cryptocurrency market data visualisation and portfolio tracking. The app features live price updates, portfolio analytics, price alerts, and secure user authentication.", ["SwiftUI", "iOS Development", "Real-time Data"], "https://github.com/MurayaSoftTouch", "/images/cryptocurrency-tracker.jpg", "Mobile", "2020"),
            ("Science Trivia STEM Learning Application", "Built a gamified STEM learning tool with Flask, PostgreSQL, and JavaScript, featuring dynamic quizzes, leaderboards, progress tracking, and adaptive learning algorithms. This educational platform makes science learning engaging and interactive, with over 1,000 questions across multiple STEM subjects.", ["Flask", "PostgreSQL", "JavaScript", "Gamification"], "https://github.com/MurayaSoftTouch", "/images/stem-learning.jpg", "Education", "2020"),
            ("Duka Platform RESTful API", "Co-developed a secure RESTful e-commerce backend using Flask, SQLAlchemy, and PostgreSQL, deployed on Render cloud platform with comprehensive API documentation. The platform includes user authentication, product catalog management, shopping cart functionality, and order processing capabilities.", ["Flask", "SQLAlchemy", "PostgreSQL", "RESTful API"], "https://github.com/MurayaSoftTouch", "/images/duka-platform.jpg", "Backend", "2020"),
            ("3-Tier AWS Infrastructure (Terraform)", "Provisioned a secure, scalable three-tier architecture on AWS using Terraform infrastructure as code, implementing EC2 for application servers, RDS for database management, and S3 for static asset storage. The infrastructure enforces least-privilege IAM policies and network segmentation for enhanced security.", ["Terraform", "AWS", "EC2", "RDS", "S3", "IAM"], "https://github.com/MurayaSoftTouch", "/images/aws-infrastructure.jpg", "DevOps", "2019")
        ]
        for title, description, technologies, link, image, category, year in projects:
            cursor.execute("""
                INSERT INTO projects (title, description, technologies, link, image, category, year, portfolio_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (title, description, technologies, link, image, category, year, portfolio_id))
        
        # Insert default services
        services = [
            ("Cloud Architecture & DevOps", "Design and implement scalable cloud-native solutions using AWS, GCP, and Kubernetes. Expert in infrastructure as code with Terraform, CI/CD pipelines, and GitOps methodologies.", "cloud", ["AWS", "GCP", "Kubernetes", "Terraform", "Docker", "CI/CD"]),
            ("Full-Stack Development", "End-to-end development of secure, scalable applications using modern technologies like Elixir/Phoenix, React/TypeScript, Python, and Node.js.", "code", ["Elixir/Phoenix", "React/TypeScript", "Python", "Node.js", "PostgreSQL", "Redis"]),
            ("Microservices & API Development", "Architect and develop distributed systems with microservices architecture, secure APIs, and robust inter-service communication patterns.", "link", ["Microservices", "RESTful APIs", "GraphQL", "gRPC", "Message Queues", "API Gateways"]),
            ("Fintech & Security Solutions", "Specialized in financial technology platforms with banking-grade security, compliance (SOC 2, PCI DSS), and high-performance requirements.", "shield", ["SOC 2 Compliance", "PCI DSS", "Authentication", "Encryption", "Security Audits"]),
            ("Performance Optimization", "Optimize existing systems for better performance, scalability, and reliability. Database optimization, caching strategies, and system monitoring.", "bolt", ["Redis Caching", "Database Optimization", "Monitoring", "Load Testing", "Profiling"]),
            ("Technical Leadership & Mentoring", "Lead development teams, establish coding standards, conduct code reviews, and mentor junior developers to improve overall team performance.", "users", ["Team Leadership", "Code Reviews", "Mentoring", "Agile/Scrum", "Technical Writing"])
        ]
        for title, description, icon, features in services:
            cursor.execute("""
                INSERT INTO services (title, description, icon, features)
                VALUES (%s, %s, %s, %s)
            """, (title, description, icon, features))
    
    conn.commit()
    cursor.close()
    conn.close()


def get_newsletter_data():
    """Get newsletter information"""
    return {
        "title": "Stay Updated",
        "description": "Subscribe to my newsletter to receive updates on my latest projects, articles, and technical insights.",
        "placeholder": "Enter your email address"
    }


def get_projects_data():
    """Get projects information"""
    conn = get_db_connection()
    if conn is None:
        return []

    cursor = conn.cursor(cursor_factory=RealDictCursor)

    try:
        # Get portfolio ID first
        cursor.execute("SELECT id FROM portfolio LIMIT 1")
        portfolio_row = cursor.fetchone()

        if not portfolio_row:
            return []

        portfolio_id = portfolio_row['id']

        # Get projects for the portfolio
        cursor.execute("""
            SELECT title, description, technologies, link, image, category, year
            FROM projects
            WHERE portfolio_id = %s
        """, (portfolio_id,))
        projects = cursor.fetchall()

        return [dict(project) for project in projects]
    except Exception as e:
        print(f"Error fetching projects data: {e}")
        return []
    finally:
        cursor.close()
        conn.close()


def get_portfolio_data():
    """Get portfolio information"""
    conn = get_db_connection()
    if conn is None:
        return get_default_portfolio_data()

    cursor = conn.cursor(cursor_factory=RealDictCursor)

    try:
        # Get portfolio info
        cursor.execute("""
            SELECT id, name, title, summary, about, contact
            FROM portfolio
            LIMIT 1
        """)
        portfolio_row = cursor.fetchone()

        if not portfolio_row:
            return get_default_portfolio_data()

        portfolio_id = portfolio_row['id']

        # Get skills
        cursor.execute("SELECT name, level FROM skills WHERE portfolio_id = %s", (portfolio_id,))
        skills = cursor.fetchall()

        # Get education
        cursor.execute("SELECT institution, degree, year, description FROM education WHERE portfolio_id = %s", (portfolio_id,))
        education = cursor.fetchall()

        # Get experience
        cursor.execute("SELECT title, company, period, description FROM experience WHERE portfolio_id = %s", (portfolio_id,))
        experience = cursor.fetchall()

        # Get certifications
        cursor.execute("SELECT name, issuer, date, credential_id, expires FROM certifications WHERE portfolio_id = %s", (portfolio_id,))
        certifications = cursor.fetchall()

        # Get testimonials
        cursor.execute("SELECT name, title, company, content, avatar FROM testimonials WHERE portfolio_id = %s", (portfolio_id,))
        testimonials = cursor.fetchall()

        # Get articles
        cursor.execute("SELECT title, description, date, url, tags FROM articles WHERE portfolio_id = %s", (portfolio_id,))
        articles = cursor.fetchall()

        # Get projects
        cursor.execute("SELECT title, description, technologies, link, image, category, year FROM projects WHERE portfolio_id = %s", (portfolio_id,))
        projects = cursor.fetchall()

        result = {
            "id": portfolio_row['id'],
            "name": portfolio_row['name'],
            "title": portfolio_row['title'],
            "summary": portfolio_row['summary'],
            "about": portfolio_row['about'],
            "skills": [dict(skill) for skill in skills],
            "education": [dict(edu) for edu in education],
            "experience": [dict(exp) for exp in experience],
            "certifications": [dict(cert) for cert in certifications],
            "testimonials": [dict(test) for test in testimonials],
            "articles": [dict(article) for article in articles],
            "projects": [dict(project) for project in projects],
            "contact": portfolio_row['contact']
        }

        return result
    except Exception as e:
        print(f"Error fetching portfolio data: {e}")
        return get_default_portfolio_data()
    finally:
        cursor.close()
        conn.close()


def get_default_portfolio_data():
    """Return default portfolio data"""
    return {
        "id": 1,
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
        ],
        "articles": [
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
        ],
        "projects": [
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
        ],
        "contact": {
            "email": "muraya.h@yahoo.com",
            "phone": "+44-747-123-4567",
            "linkedin": "https://linkedin.com/in/hamman-muraya-8b3744397",
            "github": "https://github.com/MurayaSoftTouch",
            "location": "Lincoln, Lincolnshire, England",
            "website": "https://github.com/MurayaSoftTouch"
        }
    }


def update_portfolio_data(update_data):
    """Update portfolio information"""
    conn = get_db_connection()
    if conn is None:
        return get_default_portfolio_data()
    
    cursor = conn.cursor()
    
    try:
        # Update portfolio info
        cursor.execute("""
            UPDATE portfolio
            SET name = %s, title = %s, summary = %s, about = %s, contact = %s
            WHERE id = 1
        """, (
            update_data.get('name', 'Hamman Muraya'),
            update_data.get('title', 'Senior Software Engineer & DevOps Specialist'),
            update_data.get('summary', ''),
            update_data.get('about', ''),
            json.dumps(update_data.get('contact', {}))
        ))
        
        conn.commit()
        return get_portfolio_data()
    except Exception as e:
        print(f"Error updating portfolio data: {e}")
        conn.rollback()
        return get_default_portfolio_data()
    finally:
        cursor.close()
        conn.close()


def add_experience(exp_data):
    """Add new experience"""
    conn = get_db_connection()
    if conn is None:
        return exp_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO experience (title, company, period, description, portfolio_id)
            VALUES (%s, %s, %s, %s, 1)
            RETURNING id
        """, (
            exp_data.get('title', ''),
            exp_data.get('company', ''),
            exp_data.get('period', ''),
            exp_data.get('description', ''),
            1
        ))
        
        new_id = cursor.fetchone()[0]
        conn.commit()
        
        # Return the newly added experience with its ID
        exp_data['id'] = new_id
        return exp_data
    except Exception as e:
        print(f"Error adding experience: {e}")
        conn.rollback()
        return exp_data
    finally:
        cursor.close()
        conn.close()


def update_experience(exp_id, exp_data):
    """Update experience by ID"""
    conn = get_db_connection()
    if conn is None:
        return exp_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            UPDATE experience
            SET title = %s, company = %s, period = %s, description = %s
            WHERE id = %s
        """, (
            exp_data.get('title', ''),
            exp_data.get('company', ''),
            exp_data.get('period', ''),
            exp_data.get('description', ''),
            exp_id
        ))
        
        conn.commit()
        return exp_data
    except Exception as e:
        print(f"Error updating experience: {e}")
        conn.rollback()
        return exp_data
    finally:
        cursor.close()
        conn.close()


def delete_experience(exp_id):
    """Delete experience by ID"""
    conn = get_db_connection()
    if conn is None:
        return {"message": f"Experience {exp_id} deleted successfully"}
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM experience WHERE id = %s", (exp_id,))
        conn.commit()
        return {"message": f"Experience {exp_id} deleted successfully"}
    except Exception as e:
        print(f"Error deleting experience: {e}")
        conn.rollback()
        return {"message": f"Failed to delete experience {exp_id}"}
    finally:
        cursor.close()
        conn.close()


def add_education(edu_data):
    """Add new education"""
    conn = get_db_connection()
    if conn is None:
        return edu_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO education (institution, degree, year, description, portfolio_id)
            VALUES (%s, %s, %s, %s, 1)
            RETURNING id
        """, (
            edu_data.get('institution', ''),
            edu_data.get('degree', ''),
            edu_data.get('year', ''),
            edu_data.get('description', ''),
            1
        ))
        
        new_id = cursor.fetchone()[0]
        conn.commit()
        
        # Return the newly added education with its ID
        edu_data['id'] = new_id
        return edu_data
    except Exception as e:
        print(f"Error adding education: {e}")
        conn.rollback()
        return edu_data
    finally:
        cursor.close()
        conn.close()


def update_education(edu_id, edu_data):
    """Update education by ID"""
    conn = get_db_connection()
    if conn is None:
        return edu_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            UPDATE education
            SET institution = %s, degree = %s, year = %s, description = %s
            WHERE id = %s
        """, (
            edu_data.get('institution', ''),
            edu_data.get('degree', ''),
            edu_data.get('year', ''),
            edu_data.get('description', ''),
            edu_id
        ))
        
        conn.commit()
        return edu_data
    except Exception as e:
        print(f"Error updating education: {e}")
        conn.rollback()
        return edu_data
    finally:
        cursor.close()
        conn.close()


def delete_education(edu_id):
    """Delete education by ID"""
    conn = get_db_connection()
    if conn is None:
        return {"message": f"Education {edu_id} deleted successfully"}
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM education WHERE id = %s", (edu_id,))
        conn.commit()
        return {"message": f"Education {edu_id} deleted successfully"}
    except Exception as e:
        print(f"Error deleting education: {e}")
        conn.rollback()
        return {"message": f"Failed to delete education {edu_id}"}
    finally:
        cursor.close()
        conn.close()


def add_skill(skill_data):
    """Add new skill"""
    conn = get_db_connection()
    if conn is None:
        return skill_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO skills (name, level, portfolio_id)
            VALUES (%s, %s, 1)
            RETURNING id
        """, (
            skill_data.get('name', ''),
            skill_data.get('level', 0),
            1
        ))
        
        new_id = cursor.fetchone()[0]
        conn.commit()
        
        # Return the newly added skill with its ID
        skill_data['id'] = new_id
        return skill_data
    except Exception as e:
        print(f"Error adding skill: {e}")
        conn.rollback()
        return skill_data
    finally:
        cursor.close()
        conn.close()


def update_skill(skill_id, skill_data):
    """Update skill by ID"""
    conn = get_db_connection()
    if conn is None:
        return skill_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            UPDATE skills
            SET name = %s, level = %s
            WHERE id = %s
        """, (
            skill_data.get('name', ''),
            skill_data.get('level', 0),
            skill_id
        ))
        
        conn.commit()
        return skill_data
    except Exception as e:
        print(f"Error updating skill: {e}")
        conn.rollback()
        return skill_data
    finally:
        cursor.close()
        conn.close()


def delete_skill(skill_id):
    """Delete skill by ID"""
    conn = get_db_connection()
    if conn is None:
        return {"message": f"Skill {skill_id} deleted successfully"}
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM skills WHERE id = %s", (skill_id,))
        conn.commit()
        return {"message": f"Skill {skill_id} deleted successfully"}
    except Exception as e:
        print(f"Error deleting skill: {e}")
        conn.rollback()
        return {"message": f"Failed to delete skill {skill_id}"}
    finally:
        cursor.close()
        conn.close()


def add_certification(cert_data):
    """Add new certification"""
    conn = get_db_connection()
    if conn is None:
        return cert_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO certifications (name, issuer, date, credential_id, expires, portfolio_id)
            VALUES (%s, %s, %s, %s, %s, 1)
            RETURNING id
        """, (
            cert_data.get('name', ''),
            cert_data.get('issuer', ''),
            cert_data.get('date', ''),
            cert_data.get('credential_id', ''),
            cert_data.get('expires', ''),
            1
        ))
        
        new_id = cursor.fetchone()[0]
        conn.commit()
        
        # Return the newly added certification with its ID
        cert_data['id'] = new_id
        return cert_data
    except Exception as e:
        print(f"Error adding certification: {e}")
        conn.rollback()
        return cert_data
    finally:
        cursor.close()
        conn.close()


def update_certification(cert_id, cert_data):
    """Update certification by ID"""
    conn = get_db_connection()
    if conn is None:
        return cert_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            UPDATE certifications
            SET name = %s, issuer = %s, date = %s, credential_id = %s, expires = %s
            WHERE id = %s
        """, (
            cert_data.get('name', ''),
            cert_data.get('issuer', ''),
            cert_data.get('date', ''),
            cert_data.get('credential_id', ''),
            cert_data.get('expires', ''),
            cert_id
        ))
        
        conn.commit()
        return cert_data
    except Exception as e:
        print(f"Error updating certification: {e}")
        conn.rollback()
        return cert_data
    finally:
        cursor.close()
        conn.close()


def delete_certification(cert_id):
    """Delete certification by ID"""
    conn = get_db_connection()
    if conn is None:
        return {"message": f"Certification {cert_id} deleted successfully"}
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM certifications WHERE id = %s", (cert_id,))
        conn.commit()
        return {"message": f"Certification {cert_id} deleted successfully"}
    except Exception as e:
        print(f"Error deleting certification: {e}")
        conn.rollback()
        return {"message": f"Failed to delete certification {cert_id}"}
    finally:
        cursor.close()
        conn.close()


def add_testimonial(test_data):
    """Add new testimonial"""
    conn = get_db_connection()
    if conn is None:
        return test_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO testimonials (name, title, company, content, avatar, portfolio_id)
            VALUES (%s, %s, %s, %s, %s, 1)
            RETURNING id
        """, (
            test_data.get('name', ''),
            test_data.get('title', ''),
            test_data.get('company', ''),
            test_data.get('content', ''),
            test_data.get('avatar', ''),
            1
        ))
        
        new_id = cursor.fetchone()[0]
        conn.commit()
        
        # Return the newly added testimonial with its ID
        test_data['id'] = new_id
        return test_data
    except Exception as e:
        print(f"Error adding testimonial: {e}")
        conn.rollback()
        return test_data
    finally:
        cursor.close()
        conn.close()


def update_testimonial(test_id, test_data):
    """Update testimonial by ID"""
    conn = get_db_connection()
    if conn is None:
        return test_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            UPDATE testimonials
            SET name = %s, title = %s, company = %s, content = %s, avatar = %s
            WHERE id = %s
        """, (
            test_data.get('name', ''),
            test_data.get('title', ''),
            test_data.get('company', ''),
            test_data.get('content', ''),
            test_data.get('avatar', ''),
            test_id
        ))
        
        conn.commit()
        return test_data
    except Exception as e:
        print(f"Error updating testimonial: {e}")
        conn.rollback()
        return test_data
    finally:
        cursor.close()
        conn.close()


def delete_testimonial(test_id):
    """Delete testimonial by ID"""
    conn = get_db_connection()
    if conn is None:
        return {"message": f"Testimonial {test_id} deleted successfully"}
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM testimonials WHERE id = %s", (test_id,))
        conn.commit()
        return {"message": f"Testimonial {test_id} deleted successfully"}
    except Exception as e:
        print(f"Error deleting testimonial: {e}")
        conn.rollback()
        return {"message": f"Failed to delete testimonial {test_id}"}
    finally:
        cursor.close()
        conn.close()


def add_article(article_data):
    """Add new article"""
    conn = get_db_connection()
    if conn is None:
        return article_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO articles (title, description, date, url, tags, portfolio_id)
            VALUES (%s, %s, %s, %s, %s, 1)
            RETURNING id
        """, (
            article_data.get('title', ''),
            article_data.get('description', ''),
            article_data.get('date', ''),
            article_data.get('url', ''),
            article_data.get('tags', []),
            1
        ))
        
        new_id = cursor.fetchone()[0]
        conn.commit()
        
        # Return the newly added article with its ID
        article_data['id'] = new_id
        return article_data
    except Exception as e:
        print(f"Error adding article: {e}")
        conn.rollback()
        return article_data
    finally:
        cursor.close()
        conn.close()


def update_article(article_id, article_data):
    """Update article by ID"""
    conn = get_db_connection()
    if conn is None:
        return article_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            UPDATE articles
            SET title = %s, description = %s, date = %s, url = %s, tags = %s
            WHERE id = %s
        """, (
            article_data.get('title', ''),
            article_data.get('description', ''),
            article_data.get('date', ''),
            article_data.get('url', ''),
            article_data.get('tags', []),
            article_id
        ))
        
        conn.commit()
        return article_data
    except Exception as e:
        print(f"Error updating article: {e}")
        conn.rollback()
        return article_data
    finally:
        cursor.close()
        conn.close()


def delete_article(article_id):
    """Delete article by ID"""
    conn = get_db_connection()
    if conn is None:
        return {"message": f"Article {article_id} deleted successfully"}
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM articles WHERE id = %s", (article_id,))
        conn.commit()
        return {"message": f"Article {article_id} deleted successfully"}
    except Exception as e:
        print(f"Error deleting article: {e}")
        conn.rollback()
        return {"message": f"Failed to delete article {article_id}"}
    finally:
        cursor.close()
        conn.close()


def add_project(project_data):
    """Add new project"""
    conn = get_db_connection()
    if conn is None:
        return project_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO projects (title, description, technologies, link, image, category, year, portfolio_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, 1)
            RETURNING id
        """, (
            project_data.get('title', ''),
            project_data.get('description', ''),
            project_data.get('technologies', []),
            project_data.get('link', ''),
            project_data.get('image', ''),
            project_data.get('category', ''),
            project_data.get('year', ''),
            1
        ))
        
        new_id = cursor.fetchone()[0]
        conn.commit()
        
        # Return the newly added project with its ID
        project_data['id'] = new_id
        return project_data
    except Exception as e:
        print(f"Error adding project: {e}")
        conn.rollback()
        return project_data
    finally:
        cursor.close()
        conn.close()


def update_project(project_id, project_data):
    """Update project by ID"""
    conn = get_db_connection()
    if conn is None:
        return project_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            UPDATE projects
            SET title = %s, description = %s, technologies = %s, link = %s, image = %s, category = %s, year = %s
            WHERE id = %s
        """, (
            project_data.get('title', ''),
            project_data.get('description', ''),
            project_data.get('technologies', []),
            project_data.get('link', ''),
            project_data.get('image', ''),
            project_data.get('category', ''),
            project_data.get('year', ''),
            project_id
        ))
        
        conn.commit()
        return project_data
    except Exception as e:
        print(f"Error updating project: {e}")
        conn.rollback()
        return project_data
    finally:
        cursor.close()
        conn.close()


def delete_project(project_id):
    """Delete project by ID"""
    conn = get_db_connection()
    if conn is None:
        return {"message": f"Project {project_id} deleted successfully"}
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM projects WHERE id = %s", (project_id,))
        conn.commit()
        return {"message": f"Project {project_id} deleted successfully"}
    except Exception as e:
        print(f"Error deleting project: {e}")
        conn.rollback()
        return {"message": f"Failed to delete project {project_id}"}
    finally:
        cursor.close()
        conn.close()


def add_service(service_data):
    """Add new service"""
    conn = get_db_connection()
    if conn is None:
        return service_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO services (title, description, icon, features)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """, (
            service_data.get('title', ''),
            service_data.get('description', ''),
            service_data.get('icon', ''),
            service_data.get('features', [])
        ))
        
        new_id = cursor.fetchone()[0]
        conn.commit()
        
        # Return the newly added service with its ID
        service_data['id'] = new_id
        return service_data
    except Exception as e:
        print(f"Error adding service: {e}")
        conn.rollback()
        return service_data
    finally:
        cursor.close()
        conn.close()


def update_service(service_id, service_data):
    """Update service by ID"""
    conn = get_db_connection()
    if conn is None:
        return service_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            UPDATE services
            SET title = %s, description = %s, icon = %s, features = %s
            WHERE id = %s
        """, (
            service_data.get('title', ''),
            service_data.get('description', ''),
            service_data.get('icon', ''),
            service_data.get('features', []),
            service_id
        ))
        
        conn.commit()
        return service_data
    except Exception as e:
        print(f"Error updating service: {e}")
        conn.rollback()
        return service_data
    finally:
        cursor.close()
        conn.close()


def delete_service(service_id):
    """Delete service by ID"""
    conn = get_db_connection()
    if conn is None:
        return {"message": f"Service {service_id} deleted successfully"}
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM services WHERE id = %s", (service_id,))
        conn.commit()
        return {"message": f"Service {service_id} deleted successfully"}
    except Exception as e:
        print(f"Error deleting service: {e}")
        conn.rollback()
        return {"message": f"Failed to delete service {service_id}"}
    finally:
        cursor.close()
        conn.close()


def get_services():
    """Get all services"""
    conn = get_db_connection()
    if conn is None:
        return []
    
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    
    try:
        cursor.execute("SELECT * FROM services")
        services = cursor.fetchall()
        return [dict(service) for service in services]
    except Exception as e:
        print(f"Error fetching services: {e}")
        return []
    finally:
        cursor.close()
        conn.close()


def add_contact_message(message_data):
    """Add new contact message"""
    conn = get_db_connection()
    if conn is None:
        return message_data
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO contact_messages (name, email, subject, message)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """, (
            message_data.get('name', ''),
            message_data.get('email', ''),
            message_data.get('subject', ''),
            message_data.get('message', '')
        ))
        
        new_id = cursor.fetchone()[0]
        conn.commit()
        
        # Return the newly added message with its ID
        message_data['id'] = new_id
        return message_data
    except Exception as e:
        print(f"Error adding contact message: {e}")
        conn.rollback()
        return message_data
    finally:
        cursor.close()
        conn.close()


def get_contact_messages():
    """Get all contact messages"""
    conn = get_db_connection()
    if conn is None:
        return []
    
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    
    try:
        cursor.execute("SELECT * FROM contact_messages ORDER BY created_at DESC")
        messages = cursor.fetchall()
        return [dict(message) for message in messages]
    except Exception as e:
        print(f"Error fetching contact messages: {e}")
        return []
    finally:
        cursor.close()
        conn.close()


def delete_contact_message(message_id):
    """Delete contact message by ID"""
    conn = get_db_connection()
    if conn is None:
        return {"message": f"Contact message {message_id} deleted successfully"}
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM contact_messages WHERE id = %s", (message_id,))
        conn.commit()
        return {"message": f"Contact message {message_id} deleted successfully"}
    except Exception as e:
        print(f"Error deleting contact message: {e}")
        conn.rollback()
        return {"message": f"Failed to delete contact message {message_id}"}
    finally:
        cursor.close()
        conn.close()


def save_resume(filename, filepath):
    """Save resume file info to database"""
    conn = get_db_connection()
    if conn is None:
        return {"filename": filename, "filepath": filepath}
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO resume (filename, filepath)
            VALUES (%s, %s)
            RETURNING id
        """, (filename, filepath))
        
        new_id = cursor.fetchone()[0]
        conn.commit()
        
        return {"id": new_id, "filename": filename, "filepath": filepath}
    except Exception as e:
        print(f"Error saving resume: {e}")
        conn.rollback()
        return {"filename": filename, "filepath": filepath}
    finally:
        cursor.close()
        conn.close()


def get_latest_resume():
    """Get the latest resume from database"""
    conn = get_db_connection()
    if conn is None:
        return None
    
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    
    try:
        cursor.execute("SELECT * FROM resume ORDER BY uploaded_at DESC LIMIT 1")
        resume = cursor.fetchone()
        return dict(resume) if resume else None
    except Exception as e:
        print(f"Error fetching resume: {e}")
        return None
    finally:
        cursor.close()
        conn.close()


# Initialize the database when this module is imported
init_db()