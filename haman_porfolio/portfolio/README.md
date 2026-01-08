# Hamman Muraya - Portfolio

A modern portfolio website showcasing the skills and projects of Hamman Muraya, Senior Software Engineer & DevOps Specialist.

## Features

- Responsive design with modern UI
- Project showcase with detailed descriptions and category filtering
- Contact form with backend integration
- Skills visualization with progress bars
- Work experience timeline
- Professional certifications display
- Testimonials section
- Articles and publications
- Newsletter subscription
- Resume download functionality
- Dark/Light mode toggle
- Social media integration

## Tech Stack

### Backend
- Python Flask
- Flask-RESTful for API endpoints
- Flask-CORS for cross-origin requests

### Frontend
- React.js
- React Router for navigation
- CSS3 for styling
- Context API for state management

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd portfolio/backend
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the backend server:
   ```bash
   python run.py
   ```
   The backend will be available at http://localhost:5000

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd portfolio/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a .env file in the frontend directory with the following content:
   ```
   REACT_APP_API_URL=http://localhost:5000/api
   REACT_APP_CONTACT_EMAIL=muraya.h@yahoo.com
   REACT_APP_CONTACT_PHONE=+44-747-123-4567
   REACT_APP_CONTACT_LOCATION=Lincoln, Lincolnshire, England
   REACT_APP_LINKEDIN_URL=https://linkedin.com/in/hamman-muraya-8b3744397
   REACT_APP_GITHUB_URL=https://github.com/MurayaSoftTouch
   REACT_APP_TWITTER_URL=https://twitter.com/hammanmuraya
   ```

4. Start the development server:
   ```bash
   npm start
   ```
   The frontend will be available at http://localhost:3000

## API Endpoints

- `GET /api/portfolio` - Get portfolio information
- `GET /api/projects` - Get all projects
- `POST /api/projects` - Add a new project (admin only)
- `GET /api/contact` - Get contact information
- `POST /api/contact` - Submit contact form
- `GET /api/experience` - Get work experience
- `GET /api/certifications` - Get certifications
- `GET /api/testimonials` - Get testimonials
- `GET /api/articles` - Get articles
- `GET /api/newsletter` - Get newsletter information
- `POST /api/newsletter` - Subscribe to newsletter

## Environment Variables

For the backend, you can set the following environment variables:
- `PORT` - Port number for the server (default: 5000)

For the frontend, set the following in your .env file:
- `REACT_APP_API_URL` - Backend API URL
- `REACT_APP_CONTACT_EMAIL` - Contact email
- `REACT_APP_CONTACT_PHONE` - Contact phone
- `REACT_APP_CONTACT_LOCATION` - Contact location
- `REACT_APP_LINKEDIN_URL` - LinkedIn profile URL
- `REACT_APP_GITHUB_URL` - GitHub profile URL
- `REACT_APP_TWITTER_URL` - Twitter profile URL

## CI/CD Pipeline

This project includes comprehensive CI/CD configurations for multiple platforms:

### GitHub Actions
- Located in `.github/workflows/ci-cd.yml`
- Runs tests for both backend and frontend
- Performs linting and code quality checks
- Builds Docker images
- Deploys to staging and production environments

### Jenkins
- Located in `Jenkinsfile`
- Complete pipeline with testing, linting, building, and deployment stages
- Supports Docker image building and registry pushing
- Includes manual approval for production deployment

### GitLab CI
- Located in `.gitlab-ci.yml`
- Multi-stage pipeline with test, lint, build, and deploy stages
- Includes Docker image building
- Supports environment-based deployments

## Deployment

### Docker
The application can be deployed using Docker and docker-compose:

```bash
docker-compose up -d
```

### CI/CD Deployment
The CI/CD pipeline supports deployment to staging and production environments. The configuration includes:
- Automated testing
- Code quality checks
- Docker image building
- Staging deployment
- Production deployment with manual approval

### Backend
The backend can be deployed to any Python hosting service. Make sure to install the dependencies and run with a WSGI server like Gunicorn.

### Frontend
The frontend can be built for production using:
```bash
npm run build
```

## About Hamman Muraya

Hamman Muraya is a Senior Software Engineer & DevOps Specialist with over 8 years of experience designing, building, and deploying secure, scalable cloud-native systems for fintech and SaaS organisations. He holds a PhD in Software Engineering and has expertise in multiple programming languages, cloud platforms, and DevOps practices.

