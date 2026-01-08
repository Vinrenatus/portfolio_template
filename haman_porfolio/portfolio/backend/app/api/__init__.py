from flask_restful import Api
from app.api.portfolio import PortfolioAPI, AboutAPI, ContactAPI, ProjectAPI, ExperienceAPI, EducationAPI, SkillsAPI, CertificationAPI, CertificateFileAPI, ResumeAPI, TestimonialAPI, ArticleAPI, NewsletterAPI, ServicesAPI, ContactMessagesAPI
from app.api.auth import AuthAPI


def register_routes(api: Api):
    """Register all API routes"""
    api.add_resource(PortfolioAPI, "/api/portfolio")
    api.add_resource(AboutAPI, "/api/about")
    api.add_resource(EducationAPI, "/api/education")
    api.add_resource(SkillsAPI, "/api/skills")
    api.add_resource(ProjectAPI, "/api/projects")
    api.add_resource(ContactAPI, "/api/contact")
    api.add_resource(ExperienceAPI, "/api/experience")
    api.add_resource(CertificationAPI, "/api/certifications")
    api.add_resource(CertificateFileAPI, "/api/certificates/<string:filename>")
    api.add_resource(ResumeAPI, "/api/resume")
    api.add_resource(TestimonialAPI, "/api/testimonials")
    api.add_resource(ArticleAPI, "/api/articles")
    api.add_resource(NewsletterAPI, "/api/newsletter")
    api.add_resource(ServicesAPI, "/api/services")
    api.add_resource(ContactMessagesAPI, "/api/contact-messages")
    api.add_resource(AuthAPI, "/api/auth")

