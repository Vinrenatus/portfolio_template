from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields

db = SQLAlchemy()

# Define models
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.Text)
    about = db.Column(db.Text)
    contact = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    skills = db.relationship('Skill', backref='portfolio', lazy=True, cascade='all, delete-orphan')
    education = db.relationship('Education', backref='portfolio', lazy=True, cascade='all, delete-orphan')
    experience = db.relationship('Experience', backref='portfolio', lazy=True, cascade='all, delete-orphan')
    certifications = db.relationship('Certification', backref='portfolio', lazy=True, cascade='all, delete-orphan')
    testimonials = db.relationship('Testimonial', backref='portfolio', lazy=True, cascade='all, delete-orphan')
    articles = db.relationship('Article', backref='portfolio', lazy=True, cascade='all, delete-orphan')
    projects = db.relationship('Project', backref='portfolio', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        try:
            name = getattr(self, 'name', 'Unknown')
            title = getattr(self, 'title', 'Unknown')
            return f"<Portfolio(id={getattr(self, 'id', 'None')}, name='{name}', title='{title}')>"
        except Exception as e:
            return f"<Portfolio(id={getattr(self, 'id', 'None')}, error='{str(e)}')>"


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    level = db.Column(db.Integer, nullable=False)  # 0-100
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'), nullable=False)

    def __repr__(self):
        try:
            name = getattr(self, 'name', 'Unknown')
            level = getattr(self, 'level', 'Unknown')
            return f"<Skill(id={getattr(self, 'id', 'None')}, name='{name}', level={level})>"
        except Exception as e:
            return f"<Skill(id={getattr(self, 'id', 'None')}, error='{str(e)}')>"


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(255), nullable=False)
    degree = db.Column(db.String(255), nullable=False)
    year = db.Column(db.String(100))  # Increased length to accommodate longer values
    description = db.Column(db.Text)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'), nullable=False)

    def __repr__(self):
        try:
            institution = getattr(self, 'institution', 'Unknown')
            degree = getattr(self, 'degree', 'Unknown')
            year = getattr(self, 'year', 'Unknown')
            return f"<Education(id={getattr(self, 'id', 'None')}, institution='{institution}', degree='{degree}', year='{year}')>"
        except Exception as e:
            return f"<Education(id={getattr(self, 'id', 'None')}, error='{str(e)}')>"


class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(255), nullable=False)
    period = db.Column(db.String(200))  # Increased length to accommodate longer periods
    description = db.Column(db.Text)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'), nullable=False)

    def __repr__(self):
        try:
            title = getattr(self, 'title', 'Unknown')
            company = getattr(self, 'company', 'Unknown')
            period = getattr(self, 'period', 'Unknown')
            return f"<Experience(id={getattr(self, 'id', 'None')}, title='{title}', company='{company}', period='{period}')>"
        except Exception as e:
            return f"<Experience(id={getattr(self, 'id', 'None')}, error='{str(e)}')>"


class Certification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    issuer = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(50))
    credential_id = db.Column(db.String(100))
    expires = db.Column(db.String(50))
    url = db.Column(db.String(500), nullable=True)  # URL to the certificate, nullable for missing column
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'), nullable=False)

    def __repr__(self):
        try:
            name = getattr(self, 'name', 'Unknown')
            issuer = getattr(self, 'issuer', 'Unknown')
            date = getattr(self, 'date', 'Unknown')
            return f"<Certification(id={getattr(self, 'id', 'None')}, name='{name}', issuer='{issuer}', date='{date}')>"
        except Exception as e:
            return f"<Certification(id={getattr(self, 'id', 'None')}, error='{str(e)}')>"


class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255))
    company = db.Column(db.String(255))
    content = db.Column(db.Text, nullable=False)
    avatar = db.Column(db.String(255))
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'), nullable=False)

    def __repr__(self):
        try:
            name = getattr(self, 'name', 'Unknown')
            title = getattr(self, 'title', 'Unknown')
            company = getattr(self, 'company', 'Unknown')
            return f"<Testimonial(id={getattr(self, 'id', 'None')}, name='{name}', title='{title}', company='{company}')>"
        except Exception as e:
            return f"<Testimonial(id={getattr(self, 'id', 'None')}, error='{str(e)}')>"


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.String(50))
    url = db.Column(db.String(500))
    tags = db.Column(db.ARRAY(db.String))
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'), nullable=False)

    def __repr__(self):
        try:
            title = getattr(self, 'title', 'Unknown')
            date = getattr(self, 'date', 'Unknown')
            return f"<Article(id={getattr(self, 'id', 'None')}, title='{title}', date='{date}')>"
        except Exception as e:
            return f"<Article(id={getattr(self, 'id', 'None')}, error='{str(e)}')>"


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    technologies = db.Column(db.ARRAY(db.String))
    link = db.Column(db.String(500))
    image = db.Column(db.String(255))
    category = db.Column(db.String(100))
    year = db.Column(db.String(20))
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'), nullable=False)

    def __repr__(self):
        try:
            title = getattr(self, 'title', 'Unknown')
            category = getattr(self, 'category', 'Unknown')
            year = getattr(self, 'year', 'Unknown')
            return f"<Project(id={getattr(self, 'id', 'None')}, title='{title}', category='{category}', year='{year}')>"
        except Exception as e:
            return f"<Project(id={getattr(self, 'id', 'None')}, error='{str(e)}')>"


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(100))
    features = db.Column(db.ARRAY(db.String))

    def __repr__(self):
        try:
            title = getattr(self, 'title', 'Unknown')
            icon = getattr(self, 'icon', 'Unknown')
            return f"<Service(id={getattr(self, 'id', 'None')}, title='{title}', icon='{icon}')>"
        except Exception as e:
            return f"<Service(id={getattr(self, 'id', 'None')}, error='{str(e)}')>"


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255))
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        try:
            name = getattr(self, 'name', 'Unknown')
            email = getattr(self, 'email', 'Unknown')
            subject = getattr(self, 'subject', 'Unknown')
            return f"<ContactMessage(id={getattr(self, 'id', 'None')}, name='{name}', email='{email}', subject='{subject}')>"
        except Exception as e:
            return f"<ContactMessage(id={getattr(self, 'id', 'None')}, error='{str(e)}')>"


class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    filepath = db.Column(db.String(500), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        try:
            filename = getattr(self, 'filename', 'Unknown')
            filepath = getattr(self, 'filepath', 'Unknown')
            return f"<Resume(id={getattr(self, 'id', 'None')}, filename='{filename}', filepath='{filepath}')>"
        except Exception as e:
            return f"<Resume(id={getattr(self, 'id', 'None')}, error='{str(e)}')>"


# Marshmallow schemas for serialization
class SkillSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    level = fields.Int(required=True)


class EducationSchema(Schema):
    id = fields.Int(dump_only=True)
    institution = fields.Str(required=True)
    degree = fields.Str(required=True)
    year = fields.Str()
    description = fields.Str()


class ExperienceSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    company = fields.Str(required=True)
    period = fields.Str()
    description = fields.Str()


class CertificationSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    issuer = fields.Str(required=True)
    date = fields.Str()
    credential_id = fields.Str()
    expires = fields.Str()
    url = fields.Str(allow_none=True)  # URL to the certificate


class TestimonialSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    title = fields.Str()
    company = fields.Str()
    content = fields.Str(required=True)
    avatar = fields.Str()


class ArticleSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    date = fields.Str()
    url = fields.Url()
    tags = fields.List(fields.Str())


class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    technologies = fields.List(fields.Str())
    link = fields.Url()
    image = fields.Str()
    category = fields.Str()
    year = fields.Str()


class ServiceSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    icon = fields.Str()
    features = fields.List(fields.Str())


class ContactMessageSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    subject = fields.Str()
    message = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)


class ResumeSchema(Schema):
    id = fields.Int(dump_only=True)
    filename = fields.Str(required=True)
    filepath = fields.Str(required=True)
    uploaded_at = fields.DateTime(dump_only=True)


class PortfolioSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    title = fields.Str(required=True)
    summary = fields.Str()
    about = fields.Str()
    contact = fields.Dict()
    skills = fields.Nested(SkillSchema, many=True)
    education = fields.Nested(EducationSchema, many=True)
    experience = fields.Nested(ExperienceSchema, many=True)
    certifications = fields.Nested(CertificationSchema, many=True)
    testimonials = fields.Nested(TestimonialSchema, many=True)
    articles = fields.Nested(ArticleSchema, many=True)
    projects = fields.Nested(ProjectSchema, many=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


# Admin user model
class AdminUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        try:
            email = getattr(self, 'email', 'Unknown')
            is_active = getattr(self, 'is_active', 'Unknown')
            return f"<AdminUser(id={getattr(self, 'id', 'None')}, email='{email}', is_active={is_active})>"
        except Exception as e:
            return f"<AdminUser(id={getattr(self, 'id', 'None')}, error='{str(e)}')>"

    def check_password(self, password):
        """Check if provided password matches the stored hash"""
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)


# Newsletter subscriber model
class NewsletterSubscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    subscribed_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        try:
            email = getattr(self, 'email', 'Unknown')
            return f"<NewsletterSubscriber(id={getattr(self, 'id', 'None')}, email='{email}')>"
        except Exception as e:
            return f"<NewsletterSubscriber(id={getattr(self, 'id', 'None')}, error='{str(e)}')>"


# Admin user schema
class AdminUserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    created_at = fields.DateTime(dump_only=True)
    last_login = fields.DateTime(dump_only=True)
    is_active = fields.Bool()


# Newsletter subscriber schema
class NewsletterSubscriberSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    subscribed_at = fields.DateTime(dump_only=True)


# Create schemas
portfolio_schema = PortfolioSchema()
portfolios_schema = PortfolioSchema(many=True)
skill_schema = SkillSchema()
skills_schema = SkillSchema(many=True)
education_schema = EducationSchema()
educations_schema = EducationSchema(many=True)
experience_schema = ExperienceSchema()
experiences_schema = ExperienceSchema(many=True)
certification_schema = CertificationSchema()
certifications_schema = CertificationSchema(many=True)
testimonial_schema = TestimonialSchema()
testimonials_schema = TestimonialSchema(many=True)
article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)
service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)
contact_message_schema = ContactMessageSchema()
contact_messages_schema = ContactMessageSchema(many=True)
resume_schema = ResumeSchema()
resumes_schema = ResumeSchema(many=True)
admin_user_schema = AdminUserSchema()
admin_users_schema = AdminUserSchema(many=True)
newsletter_subscriber_schema = NewsletterSubscriberSchema()
newsletter_subscribers_schema = NewsletterSubscriberSchema(many=True)