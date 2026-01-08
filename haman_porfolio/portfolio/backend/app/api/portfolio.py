from flask_restful import Resource, reqparse
from flask import request, send_file
import json
from datetime import datetime
from decimal import Decimal
from app import db
from app.models import Portfolio, Skill, Education, Experience, Certification, Testimonial, Article, Project, Service, ContactMessage, Resume, NewsletterSubscriber
from app.models import portfolio_schema, portfolios_schema, skill_schema, skills_schema, education_schema, educations_schema, experience_schema, experiences_schema
from app.models import certification_schema, certifications_schema, testimonial_schema, testimonials_schema, article_schema, articles_schema
from app.models import project_schema, projects_schema, service_schema, services_schema, contact_message_schema, contact_messages_schema
from app.models import resume_schema, resumes_schema, newsletter_subscriber_schema, newsletter_subscribers_schema
from app.utils.auth import admin_required
from app.utils.email import send_contact_acknowledgment_email, send_subscription_confirmation_email
import os
from werkzeug.utils import secure_filename
import uuid


def get_projects_data():
    """Get projects information from portfolio data"""
    portfolio = Portfolio.query.first()
    if portfolio:
        return [project for project in portfolio.projects]
    return []


class PortfolioAPI(Resource):
    def get(self):
        """Get portfolio information"""
        portfolio = Portfolio.query.first()
        if portfolio:
            return portfolio_schema.dump(portfolio)
        else:
            # Return default portfolio data if none exists
            return {
                "id": 1,
                "name": "Hamman Muraya",
                "title": "Senior Software Engineer & DevOps Specialist",
                "summary": "Highly skilled and dedicated Senior Software Engineer with over 8 years of experience designing, building, and deploying secure, scalable cloud-native systems for fintech and SaaS organisations.",
                "about": "I am a highly skilled and dedicated Senior Software Engineer with over 8 years of experience designing, building, and deploying secure, scalable cloud-native systems for fintech and SaaS organisations. I am committed to delivering production-grade solutions that meet the highest standards of quality, security, and performance. Since beginning my professional career in software engineering in 2017, I have continuously strived to improve my technical expertise through advanced education, professional certifications, and hands-on experience across diverse technology stacks and cloud platforms. I am highly effective at leading and managing development teams, as well as working independently to prioritise and achieve project targets and business requirements. Throughout my career, I have successfully architected and delivered SOC 2-compliant microservices, optimised database performance for high-throughput systems, and implemented robust CI/CD pipelines using GitOps methodologies. I hold a PhD in Software Engineering from California State University (2019-2022), which enables me to blend academic rigor with practical, production-focused delivery.",
                "contact": {
                    "email": "muraya.h@yahoo.com",
                    "phone": "+44-747-123-4567",
                    "linkedin": "https://linkedin.com/in/hamman-muraya-8b3744397",
                    "github": "https://github.com/MurayaSoftTouch",
                    "location": "Lincoln, Lincolnshire, England",
                    "website": "https://github.com/MurayaSoftTouch"
                },
                "skills": [],
                "education": [],
                "experience": [],
                "certifications": [],
                "testimonials": [],
                "articles": [],
                "projects": [],
                "created_at": None,
                "updated_at": None
            }

    @admin_required
    def put(self):
        """Update portfolio information (admin only)"""
        data = request.get_json()

        # Get or create portfolio
        portfolio = Portfolio.query.first()
        if not portfolio:
            portfolio = Portfolio(
                name=data.get('name', 'Hamman Muraya'),
                title=data.get('title', 'Senior Software Engineer & DevOps Specialist'),
                summary=data.get('summary', ''),
                about=data.get('about', ''),
                contact=data.get('contact', {})
            )
            db.session.add(portfolio)
        else:
            portfolio.name = data.get('name', portfolio.name)
            portfolio.title = data.get('title', portfolio.title)
            portfolio.summary = data.get('summary', portfolio.summary)
            portfolio.about = data.get('about', portfolio.about)
            portfolio.contact = data.get('contact', portfolio.contact)

        db.session.commit()
        return portfolio_schema.dump(portfolio)


class AboutAPI(Resource):
    def get(self):
        """Get about me information"""
        portfolio = Portfolio.query.first()
        if portfolio:
            portfolio_data = portfolio_schema.dump(portfolio)
            return {"about": portfolio_data.get("about")}
        else:
            return {"about": "Default about text"}

    @admin_required
    def put(self):
        """Update about me information (admin only)"""
        try:
            data = request.get_json()
            about_text = data.get("about")

            portfolio = Portfolio.query.first()
            if not portfolio:
                return {"message": "Portfolio not found"}, 404

            portfolio.about = about_text if about_text is not None else portfolio.about
            db.session.commit()

            # Ensure we return a clean, serializable response
            return {"about": portfolio.about if portfolio.about is not None else ""}, 200
        except Exception as e:
            # Log the error for debugging
            print(f"Error in AboutAPI PUT: {str(e)}")
            # Return a proper error response
            return {"message": "Internal server error"}, 500


class ProjectAPI(Resource):
    def get(self):
        """Get all projects"""
        projects = Project.query.all()
        return {"projects": projects_schema.dump(projects)}

    @admin_required
    def post(self):
        """Add a new project (admin only)"""
        data = request.get_json()

        # Validate category
        valid_categories = ["Software Development", "DevOps Engineering", "AI Training"]
        category = data.get('category', '')
        if category not in valid_categories:
            # Default to Software Development if invalid category
            category = "Software Development"

        # Convert technologies string to array if it's a comma-separated string
        technologies = data.get('technologies', [])
        if isinstance(technologies, str):
            technologies = [tech.strip() for tech in technologies.split(',')]

        portfolio = Portfolio.query.first()
        if not portfolio:
            return {"message": "Portfolio not found"}, 404

        new_project = Project(
            title=data.get('title'),
            description=data.get('description'),
            technologies=technologies,
            link=data.get('link'),
            image=data.get('image'),
            category=category,
            year=data.get('year'),
            portfolio_id=portfolio.id
        )

        db.session.add(new_project)
        db.session.commit()

        return project_schema.dump(new_project), 201


    @admin_required
    def put(self):
        """Update a project (admin only)"""
        data = request.get_json()
        project_id = data.get("id")

        project = Project.query.get(project_id)
        if not project:
            return {"message": "Project not found"}, 404

        project.title = data.get('title', project.title)
        project.description = data.get('description', project.description)

        # Handle technologies array
        technologies = data.get('technologies', project.technologies)
        if isinstance(technologies, str):
            technologies = [tech.strip() for tech in technologies.split(',')]
        elif technologies is None:
            technologies = []
        project.technologies = technologies

        project.link = data.get('link', project.link)
        project.image = data.get('image', project.image)

        # Validate category
        valid_categories = ["Software Development", "DevOps Engineering", "AI Training"]
        category = data.get('category', project.category)
        if category in valid_categories:
            project.category = category
        else:
            project.category = project.category  # Keep existing category if invalid

        project.year = data.get('year', project.year)

        db.session.commit()

        return project_schema.dump(project), 200

    @admin_required
    def delete(self):
        """Delete a project (admin only)"""
        data = request.get_json()
        project_id = data.get("id")

        project = Project.query.get(project_id)
        if not project:
            return {"message": "Project not found"}, 404

        db.session.delete(project)
        db.session.commit()

        return {"message": f"Project {project_id} deleted successfully"}, 200


class ContactAPI(Resource):
    def get(self):
        """Get contact information"""
        portfolio = Portfolio.query.first()
        if portfolio:
            portfolio_data = portfolio_schema.dump(portfolio)
            return portfolio_data.get("contact", {})
        else:
            return {
                "email": "muraya.h@yahoo.com",
                "phone": "+44-747-123-4567",
                "linkedin": "https://linkedin.com/in/hamman-muraya-8b3744397",
                "github": "https://github.com/MurayaSoftTouch",
                "location": "Lincoln, Lincolnshire, England",
                "website": "https://github.com/MurayaSoftTouch"
            }

    def post(self):
        """Handle contact form submission"""
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name is required')
        parser.add_argument('email', type=str, required=True, help='Email is required')
        parser.add_argument('message', type=str, required=True, help='Message is required')
        parser.add_argument('subject', type=str, default='')
        args = parser.parse_args()

        name = args['name']
        email = args['email']
        message = args['message']
        subject = args['subject']

        # Create and save the contact message
        contact_message = ContactMessage(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        db.session.add(contact_message)
        db.session.commit()

        # Send acknowledgment email to the user
        try:
            send_contact_acknowledgment_email(name, email, message)
        except Exception as e:
            # Log the error but continue with the submission
            print(f"Error sending acknowledgment email: {str(e)}")

        return contact_message_schema.dump(contact_message), 201


class ExperienceAPI(Resource):
    def get(self):
        """Get work experience"""
        experiences = Experience.query.all()
        return {"experience": experiences_schema.dump(experiences)}

    @admin_required
    def post(self):
        """Add work experience (admin only)"""
        data = request.get_json()
        portfolio = Portfolio.query.first()
        if not portfolio:
            return {"message": "Portfolio not found"}, 404

        new_experience = Experience(
            title=data.get('title'),
            company=data.get('company'),
            period=data.get('period'),
            description=data.get('description'),
            portfolio_id=portfolio.id
        )

        db.session.add(new_experience)
        db.session.commit()

        return experience_schema.dump(new_experience), 201

    @admin_required
    def put(self):
        """Update work experience (admin only)"""
        data = request.get_json()
        exp_id = data.get("id")

        experience = Experience.query.get(exp_id)
        if not experience:
            return {"message": "Experience not found"}, 404

        experience.title = data.get('title', experience.title)
        experience.company = data.get('company', experience.company)
        experience.period = data.get('period', experience.period)
        experience.description = data.get('description', experience.description)

        db.session.commit()

        return experience_schema.dump(experience), 200

    @admin_required
    def delete(self):
        """Delete work experience (admin only)"""
        data = request.get_json()
        exp_id = data.get("id")

        experience = Experience.query.get(exp_id)
        if not experience:
            return {"message": "Experience not found"}, 404

        db.session.delete(experience)
        db.session.commit()

        return {"message": f"Experience {exp_id} deleted successfully"}, 200


class EducationAPI(Resource):
    def get(self):
        """Get education information"""
        educations = Education.query.all()
        return {"education": educations_schema.dump(educations)}

    @admin_required
    def post(self):
        """Add education (admin only)"""
        data = request.get_json()
        portfolio = Portfolio.query.first()
        if not portfolio:
            return {"message": "Portfolio not found"}, 404

        new_education = Education(
            institution=data.get('institution'),
            degree=data.get('degree'),
            year=data.get('year'),
            description=data.get('description'),
            portfolio_id=portfolio.id
        )

        db.session.add(new_education)
        db.session.commit()

        return education_schema.dump(new_education), 201

    @admin_required
    def put(self):
        """Update education (admin only)"""
        data = request.get_json()
        edu_id = data.get("id")

        education = Education.query.get(edu_id)
        if not education:
            return {"message": "Education not found"}, 404

        education.institution = data.get('institution', education.institution)
        education.degree = data.get('degree', education.degree)
        education.year = data.get('year', education.year)
        education.description = data.get('description', education.description)

        db.session.commit()

        return education_schema.dump(education), 200

    @admin_required
    def delete(self):
        """Delete education (admin only)"""
        data = request.get_json()
        edu_id = data.get("id")

        education = Education.query.get(edu_id)
        if not education:
            return {"message": "Education not found"}, 404

        db.session.delete(education)
        db.session.commit()

        return {"message": f"Education {edu_id} deleted successfully"}, 200


class SkillsAPI(Resource):
    def get(self):
        """Get skills information"""
        skills = Skill.query.all()
        return {"skills": skills_schema.dump(skills)}

    @admin_required
    def post(self):
        """Add skill (admin only)"""
        data = request.get_json()
        portfolio = Portfolio.query.first()
        if not portfolio:
            return {"message": "Portfolio not found"}, 404

        new_skill = Skill(
            name=data.get('name'),
            level=data.get('level'),
            portfolio_id=portfolio.id
        )

        db.session.add(new_skill)
        db.session.commit()

        return skill_schema.dump(new_skill), 201

    @admin_required
    def put(self):
        """Update skill (admin only)"""
        data = request.get_json()
        skill_id = data.get("id")

        skill = Skill.query.get(skill_id)
        if not skill:
            return {"message": "Skill not found"}, 404

        skill.name = data.get('name', skill.name)
        skill.level = data.get('level', skill.level)

        db.session.commit()

        return skill_schema.dump(skill), 200

    @admin_required
    def delete(self):
        """Delete skill (admin only)"""
        data = request.get_json()
        skill_id = data.get("id")

        skill = Skill.query.get(skill_id)
        if not skill:
            return {"message": "Skill not found"}, 404

        db.session.delete(skill)
        db.session.commit()

        return {"message": f"Skill {skill_id} deleted successfully"}, 200


# Configure upload folder
UPLOAD_FOLDER = 'uploads/certificates'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


class CertificationAPI(Resource):
    def get(self):
        """Get certifications"""
        certifications = Certification.query.all()
        return {"certifications": certifications_schema.dump(certifications)}

    @admin_required
    def post(self):
        """Add certification (admin only)"""
        if 'file' in request.files:
            file = request.files['file']
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                unique_filename = f"{str(uuid.uuid4())}_{filename}"
                file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
                file.save(file_path)

                # Get form data
                name = request.form.get('name')
                issuer = request.form.get('issuer')
                date = request.form.get('date')
                credential_id = request.form.get('credential_id')
                expires = request.form.get('expires')

                portfolio = Portfolio.query.first()
                if not portfolio:
                    return {"message": "Portfolio not found"}, 404

                # Get form data
                url = request.form.get('url')  # URL for the certificate

                # Create certification data
                cert_data = {
                    "name": name,
                    "issuer": issuer,
                    "date": date,
                    "credential_id": credential_id,
                    "expires": expires,
                    "url": url,  # URL to the certificate
                    "file_path": unique_filename  # Store the file path
                }

                new_certification = Certification(
                    name=cert_data["name"],
                    issuer=cert_data["issuer"],
                    date=cert_data["date"],
                    credential_id=cert_data["credential_id"],
                    expires=cert_data["expires"],
                    url=cert_data["url"],
                    portfolio_id=portfolio.id
                )

                db.session.add(new_certification)
                db.session.commit()

                return certification_schema.dump(new_certification), 201

        # Handle JSON data without file
        data = request.get_json()
        portfolio = Portfolio.query.first()
        if not portfolio:
            return {"message": "Portfolio not found"}, 404

        new_certification = Certification(
            name=data.get('name'),
            issuer=data.get('issuer'),
            date=data.get('date'),
            credential_id=data.get('credential_id'),
            expires=data.get('expires'),
            url=data.get('url'),  # URL to the certificate
            portfolio_id=portfolio.id
        )

        db.session.add(new_certification)
        db.session.commit()

        return certification_schema.dump(new_certification), 201

    @admin_required
    def put(self):
        """Update certification (admin only)"""
        data = request.get_json()
        cert_id = data.get("id")

        certification = Certification.query.get(cert_id)
        if not certification:
            return {"message": "Certification not found"}, 404

        certification.name = data.get('name', certification.name)
        certification.issuer = data.get('issuer', certification.issuer)
        certification.date = data.get('date', certification.date)
        certification.credential_id = data.get('credential_id', certification.credential_id)
        certification.expires = data.get('expires', certification.expires)

        # Only update URL if it's provided in the request (to handle cases where column doesn't exist yet)
        if 'url' in data:
            certification.url = data.get('url')

        db.session.commit()

        return certification_schema.dump(certification), 200

    @admin_required
    def delete(self):
        """Delete certification and associated file (admin only)"""
        data = request.get_json()
        cert_id = data.get("id")
        file_path = data.get("file_path")  # Path to the certificate file to delete
        
        # Delete file if it exists
        if file_path:
            try:
                full_path = os.path.join(UPLOAD_FOLDER, file_path)
                if os.path.exists(full_path):
                    os.remove(full_path)
            except Exception as e:
                # Log error but continue with deletion
                print(f"Error deleting file: {e}")
        
        certification = Certification.query.get(cert_id)
        if not certification:
            return {"message": "Certification not found"}, 404
        
        db.session.delete(certification)
        db.session.commit()
        
        return {"message": f"Certification {cert_id} deleted successfully"}, 200


class CertificateFileAPI(Resource):
    def get(self, filename):
        """Download certificate file"""
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return {"message": "Certificate file not found"}, 404


class TestimonialAPI(Resource):
    def get(self):
        """Get testimonials"""
        testimonials = Testimonial.query.all()
        return {"testimonials": testimonials_schema.dump(testimonials)}

    def post(self):
        """Add testimonial (client can submit)"""
        data = request.get_json()
        name = data.get("name")
        title = data.get("title")
        company = data.get("company")
        content = data.get("content")
        avatar = data.get("avatar", "")  # Optional avatar

        portfolio = Portfolio.query.first()
        if not portfolio:
            return {"message": "Portfolio not found"}, 404

        # Create testimonial data
        new_testimonial = Testimonial(
            name=name,
            title=title,
            company=company,
            content=content,
            avatar=avatar,
            portfolio_id=portfolio.id
        )

        db.session.add(new_testimonial)
        db.session.commit()

        return testimonial_schema.dump(new_testimonial), 201

    @admin_required
    def put(self):
        """Update testimonial (admin only)"""
        data = request.get_json()
        testimonial_id = data.get("id")

        testimonial = Testimonial.query.get(testimonial_id)
        if not testimonial:
            return {"message": "Testimonial not found"}, 404

        testimonial.name = data.get('name', testimonial.name)
        testimonial.title = data.get('title', testimonial.title)
        testimonial.company = data.get('company', testimonial.company)
        testimonial.content = data.get('content', testimonial.content)
        testimonial.avatar = data.get('avatar', testimonial.avatar)

        db.session.commit()

        return testimonial_schema.dump(testimonial), 200

    @admin_required
    def delete(self):
        """Delete testimonial (admin only)"""
        data = request.get_json()
        testimonial_id = data.get("id")

        testimonial = Testimonial.query.get(testimonial_id)
        if not testimonial:
            return {"message": "Testimonial not found"}, 404

        db.session.delete(testimonial)
        db.session.commit()

        return {"message": f"Testimonial {testimonial_id} deleted successfully"}, 200


class ArticleAPI(Resource):
    def get(self):
        """Get articles/blogs"""
        articles = Article.query.all()
        return {"articles": articles_schema.dump(articles)}

    @admin_required
    def post(self):
        """Add article (admin only)"""
        data = request.get_json()
        portfolio = Portfolio.query.first()
        if not portfolio:
            return {"message": "Portfolio not found"}, 404

        # Convert tags string to array if it's a comma-separated string
        tags = data.get('tags', [])
        if isinstance(tags, str):
            tags = [tag.strip() for tag in tags.split(',')]

        new_article = Article(
            title=data.get('title'),
            description=data.get('description'),
            date=data.get('date'),
            url=data.get('url'),
            tags=tags,
            portfolio_id=portfolio.id
        )

        db.session.add(new_article)
        db.session.commit()

        return article_schema.dump(new_article), 201

    @admin_required
    def put(self):
        """Update article (admin only)"""
        data = request.get_json()
        article_id = data.get("id")

        article = Article.query.get(article_id)
        if not article:
            return {"message": "Article not found"}, 404

        article.title = data.get('title', article.title)
        article.description = data.get('description', article.description)
        article.date = data.get('date', article.date)
        article.url = data.get('url', article.url)

        # Handle tags array
        tags = data.get('tags', article.tags)
        if isinstance(tags, str):
            tags = [tag.strip() for tag in tags.split(',')]
        article.tags = tags

        db.session.commit()

        return article_schema.dump(article), 200

    @admin_required
    def delete(self):
        """Delete article (admin only)"""
        data = request.get_json()
        article_id = data.get("id")

        article = Article.query.get(article_id)
        if not article:
            return {"message": "Article not found"}, 404

        db.session.delete(article)
        db.session.commit()

        return {"message": f"Article {article_id} deleted successfully"}, 200


# Configure resume upload folder
RESUME_UPLOAD_FOLDER = 'uploads/resume'
if not os.path.exists(RESUME_UPLOAD_FOLDER):
    os.makedirs(RESUME_UPLOAD_FOLDER)


class ResumeAPI(Resource):
    @admin_required
    def post(self):
        """Upload resume (admin only)"""
        if 'file' not in request.files:
            return {"message": "No file provided"}, 400

        file = request.files['file']
        if file.filename == '':
            return {"message": "No file selected"}, 400

        if file and file.filename.lower().endswith('.pdf'):
            # Generate unique filename to avoid conflicts
            unique_filename = f"resume_{uuid.uuid4().hex}.pdf"
            file_path = os.path.join(RESUME_UPLOAD_FOLDER, unique_filename)
            file.save(file_path)

            # Check if a resume already exists and delete the old file
            existing_resume = Resume.query.first()
            if existing_resume:
                old_file_path = existing_resume.filepath
                if os.path.exists(old_file_path):
                    os.remove(old_file_path)
                db.session.delete(existing_resume)

            # Create new resume record
            new_resume = Resume(
                filename=unique_filename,
                filepath=file_path
            )

            db.session.add(new_resume)
            db.session.commit()

            return resume_schema.dump(new_resume), 201
        else:
            return {"message": "Only PDF files are allowed for resume"}, 400

    def get(self):
        """Download resume (public)"""
        resume_record = Resume.query.first()
        if resume_record and os.path.exists(resume_record.filepath):
            return send_file(resume_record.filepath, as_attachment=True, download_name=resume_record.filename)
        else:
            return {"message": "Resume not available"}, 404


class NewsletterAPI(Resource):
    def get(self):
        """Get newsletter information"""
        return {
            "title": "Stay Updated",
            "description": "Subscribe to my newsletter to receive updates on my latest projects, articles, and technical insights.",
            "placeholder": "Enter your email address"
        }

    def post(self):
        """Handle newsletter subscription"""
        data = request.get_json()
        email = data.get("email")

        if not email:
            return {"message": "Email is required"}, 400

        # Check if email already exists
        existing_subscriber = NewsletterSubscriber.query.filter_by(email=email).first()
        if existing_subscriber:
            return {"message": "Email already subscribed"}, 400

        # Create new subscriber
        new_subscriber = NewsletterSubscriber(email=email)
        db.session.add(new_subscriber)
        db.session.commit()

        # Send subscription confirmation email
        try:
            send_subscription_confirmation_email(email)
        except Exception as e:
            # Log error but continue with subscription
            print(f"Error sending confirmation email: {str(e)}")

        return newsletter_subscriber_schema.dump(new_subscriber), 201


class ContactMessagesAPI(Resource):
    def get(self):
        """Get all contact messages (admin only)"""
        messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
        return {"messages": contact_messages_schema.dump(messages)}, 200

    @admin_required
    def delete(self):
        """Delete a contact message (admin only)"""
        data = request.get_json()
        message_id = data.get("id")

        message = ContactMessage.query.get(message_id)
        if not message:
            return {"message": "Message not found"}, 404

        db.session.delete(message)
        db.session.commit()

        return {"message": f"Message {message_id} deleted successfully"}, 200


class ServicesAPI(Resource):
    def get(self):
        """Get all services"""
        services = Service.query.all()
        return {"services": services_schema.dump(services)}, 200

    @admin_required
    def post(self):
        """Add a new service (admin only)"""
        data = request.get_json()

        # Convert features string to array if it's a comma-separated string
        features = data.get('features', [])
        if isinstance(features, str):
            features = [feature.strip() for feature in features.split(',')]

        new_service = Service(
            title=data.get('title'),
            description=data.get('description'),
            icon=data.get('icon'),
            features=features
        )

        db.session.add(new_service)
        db.session.commit()

        return service_schema.dump(new_service), 201

    @admin_required
    def put(self):
        """Update a service (admin only)"""
        data = request.get_json()
        service_id = data.get("id")

        service = Service.query.get(service_id)
        if not service:
            return {"message": "Service not found"}, 404

        service.title = data.get('title', service.title)
        service.description = data.get('description', service.description)
        service.icon = data.get('icon', service.icon)

        # Handle features array
        features = data.get('features', service.features)
        if isinstance(features, str):
            features = [feature.strip() for feature in features.split(',')]
        service.features = features

        db.session.commit()

        return service_schema.dump(service), 200

    @admin_required
    def delete(self):
        """Delete a service (admin only)"""
        data = request.get_json()
        service_id = data.get("id")

        service = Service.query.get(service_id)
        if not service:
            return {"message": "Service not found"}, 404

        db.session.delete(service)
        db.session.commit()

        return {"message": f"Service {service_id} deleted successfully"}, 200


