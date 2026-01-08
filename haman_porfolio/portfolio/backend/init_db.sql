-- Create the portfolio database
CREATE DATABASE portfolio_db;

-- Connect to the database
\c portfolio_db;

-- Create portfolio table
CREATE TABLE portfolio (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    summary TEXT,
    about TEXT,
    contact JSONB
);

-- Create skills table
CREATE TABLE skills (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    level INTEGER NOT NULL,
    portfolio_id INTEGER REFERENCES portfolio(id) ON DELETE CASCADE
);

-- Create education table
CREATE TABLE education (
    id SERIAL PRIMARY KEY,
    institution VARCHAR(255) NOT NULL,
    degree VARCHAR(255) NOT NULL,
    year VARCHAR(50),
    description TEXT,
    portfolio_id INTEGER REFERENCES portfolio(id) ON DELETE CASCADE
);

-- Create experience table
CREATE TABLE experience (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    company VARCHAR(255) NOT NULL,
    period VARCHAR(100),
    description TEXT,
    portfolio_id INTEGER REFERENCES portfolio(id) ON DELETE CASCADE
);

-- Create certifications table
CREATE TABLE certifications (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    issuer VARCHAR(255) NOT NULL,
    date VARCHAR(50),
    credential_id VARCHAR(100),
    expires VARCHAR(50),
    url VARCHAR(500),  -- Add URL field for certificate links
    portfolio_id INTEGER REFERENCES portfolio(id) ON DELETE CASCADE
);

-- Create testimonials table
CREATE TABLE testimonials (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    title VARCHAR(255),
    company VARCHAR(255),
    content TEXT NOT NULL,
    avatar VARCHAR(255),
    portfolio_id INTEGER REFERENCES portfolio(id) ON DELETE CASCADE
);

-- Create articles table
CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    date VARCHAR(50),
    url VARCHAR(500),
    tags TEXT[],
    portfolio_id INTEGER REFERENCES portfolio(id) ON DELETE CASCADE
);

-- Create projects table
CREATE TABLE projects (
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

-- Create services table
CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    icon VARCHAR(100),
    features TEXT[]
);

-- Create contact_messages table
CREATE TABLE contact_messages (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    subject VARCHAR(255),
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create resume table
CREATE TABLE resume (
    id SERIAL PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    filepath VARCHAR(500) NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert default portfolio data
INSERT INTO portfolio (name, title, summary, about, contact) VALUES (
    'Hamman Muraya',
    'Senior Software Engineer & DevOps Specialist',
    'Highly skilled and dedicated Senior Software Engineer with over 8 years of experience designing, building, and deploying secure, scalable cloud-native systems for fintech and SaaS organisations.',
    'I am a highly skilled and dedicated Senior Software Engineer with over 8 years of experience designing, building, and deploying secure, scalable cloud-native systems for fintech and SaaS organisations. I am committed to delivering production-grade solutions that meet the highest standards of quality, security, and performance. Since beginning my professional career in software engineering in 2017, I have continuously strived to improve my technical expertise through advanced education, professional certifications, and hands-on experience across diverse technology stacks and cloud platforms. I am highly effective at leading and managing development teams, as well as working independently to prioritise and achieve project targets and business requirements. Throughout my career, I have successfully architected and delivered SOC 2-compliant microservices, optimised database performance for high-throughput systems, and implemented robust CI/CD pipelines using GitOps methodologies. I hold a PhD in Software Engineering from California State University (2019-2022), which enables me to blend academic rigor with practical, production-focused delivery.',
    '{"email": "muraya.h@yahoo.com", "phone": "+44-747-123-4567", "linkedin": "https://linkedin.com/in/hamman-muraya-8b3744397", "github": "https://github.com/MurayaSoftTouch", "location": "Lincoln, Lincolnshire, England", "website": "https://github.com/MurayaSoftTouch"}'
);

-- Insert default services
INSERT INTO services (title, description, icon, features) VALUES
('Cloud Architecture & DevOps', 'Design and implement scalable cloud-native solutions using AWS, GCP, and Kubernetes. Expert in infrastructure as code with Terraform, CI/CD pipelines, and GitOps methodologies.', 'cloud', ARRAY['AWS', 'GCP', 'Kubernetes', 'Terraform', 'Docker', 'CI/CD']),
('Full-Stack Development', 'End-to-end development of secure, scalable applications using modern technologies like Elixir/Phoenix, React/TypeScript, Python, and Node.js.', 'code', ARRAY['Elixir/Phoenix', 'React/TypeScript', 'Python', 'Node.js', 'PostgreSQL', 'Redis']),
('Microservices & API Development', 'Architect and develop distributed systems with microservices architecture, secure APIs, and robust inter-service communication patterns.', 'link', ARRAY['Microservices', 'RESTful APIs', 'GraphQL', 'gRPC', 'Message Queues', 'API Gateways']),
('Fintech & Security Solutions', 'Specialized in financial technology platforms with banking-grade security, compliance (SOC 2, PCI DSS), and high-performance requirements.', 'shield', ARRAY['SOC 2 Compliance', 'PCI DSS', 'Authentication', 'Encryption', 'Security Audits']),
('Performance Optimization', 'Optimize existing systems for better performance, scalability, and reliability. Database optimization, caching strategies, and system monitoring.', 'bolt', ARRAY['Redis Caching', 'Database Optimization', 'Monitoring', 'Load Testing', 'Profiling']),
('Technical Leadership & Mentoring', 'Lead development teams, establish coding standards, conduct code reviews, and mentor junior developers to improve overall team performance.', 'users', ARRAY['Team Leadership', 'Code Reviews', 'Mentoring', 'Agile/Scrum', 'Technical Writing']);