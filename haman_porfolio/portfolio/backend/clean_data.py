#!/usr/bin/env python
"""
Clean up problematic data in the database
"""

from app import create_app
from app.models import db, Skill, Education, Experience, Certification, Testimonial, Article, Project, Service

def clean_database():
    app = create_app()

    with app.app_context():
        # Clean up problematic entries that contain the repeated text
        problematic_text = "9-2022), which enables me to blend academic rigor with practical, production-focused delivery."
        
        # Clean skills
        skills_to_clean = Skill.query.filter(Skill.name.like(f"%{problematic_text}%")).all()
        for skill in skills_to_clean:
            if problematic_text in skill.name:
                skill.name = skill.name.replace(problematic_text, "").strip() or "Cleaned Skill"
            if skill.name == "":
                skill.name = "Cleaned Skill"
        print(f"Cleaned {len(skills_to_clean)} skills")
        
        # Clean education
        education_to_clean = Education.query.filter(Education.institution.like(f"%{problematic_text}%") | 
                                                  Education.degree.like(f"%{problematic_text}%") |
                                                  Education.year.like(f"%{problematic_text}%")).all()
        for edu in education_to_clean:
            if problematic_text in edu.institution:
                edu.institution = edu.institution.replace(problematic_text, "").strip() or "Cleaned Institution"
            if problematic_text in edu.degree:
                edu.degree = edu.degree.replace(problematic_text, "").strip() or "Cleaned Degree"
            if problematic_text in edu.year:
                edu.year = edu.year.replace(problematic_text, "").strip() or "2023"
        print(f"Cleaned {len(education_to_clean)} education records")
        
        # Clean experience
        experience_to_clean = Experience.query.filter(Experience.company.like(f"%{problematic_text}%")).all()
        for exp in experience_to_clean:
            if problematic_text in exp.company:
                exp.company = exp.company.replace(problematic_text, "").strip() or "Cleaned Company"
        print(f"Cleaned {len(experience_to_clean)} experience records")
        
        # Clean certifications
        certifications_to_clean = Certification.query.filter(Certification.name.like(f"%{problematic_text}%") |
                                                           Certification.issuer.like(f"%{problematic_text}%") |
                                                           Certification.credential_id.like(f"%{problematic_text}%")).all()
        for cert in certifications_to_clean:
            if problematic_text in cert.name:
                cert.name = cert.name.replace(problematic_text, "").strip() or "Cleaned Certification"
            if problematic_text in cert.issuer:
                cert.issuer = cert.issuer.replace(problematic_text, "").strip() or "Cleaned Issuer"
            if problematic_text in cert.credential_id:
                cert.credential_id = cert.credential_id.replace(problematic_text, "").strip() or "CLEANED_ID"
        print(f"Cleaned {len(certifications_to_clean)} certification records")
        
        # Clean testimonials
        testimonials_to_clean = Testimonial.query.filter(Testimonial.name.like(f"%{problematic_text}%") |
                                                        Testimonial.title.like(f"%{problematic_text}%") |
                                                        Testimonial.company.like(f"%{problematic_text}%") |
                                                        Testimonial.avatar.like(f"%{problematic_text}%")).all()
        for testimonial in testimonials_to_clean:
            if problematic_text in testimonial.name:
                testimonial.name = testimonial.name.replace(problematic_text, "").strip() or "Cleaned Name"
            if problematic_text in testimonial.title:
                testimonial.title = testimonial.title.replace(problematic_text, "").strip() or "Cleaned Title"
            if problematic_text in testimonial.company:
                testimonial.company = testimonial.company.replace(problematic_text, "").strip() or "Cleaned Company"
            if problematic_text in testimonial.avatar:
                testimonial.avatar = testimonial.avatar.replace(problematic_text, "").strip() or ""
        print(f"Cleaned {len(testimonials_to_clean)} testimonial records")
        
        # Clean projects
        projects_to_clean = Project.query.filter(Project.title.like(f"%{problematic_text}%") |
                                                Project.category.like(f"%{problematic_text}%")).all()
        for project in projects_to_clean:
            if problematic_text in project.title:
                project.title = project.title.replace(problematic_text, "").strip() or "Cleaned Project"
            if problematic_text in project.category:
                project.category = project.category.replace(problematic_text, "").strip() or "Software Development"
        print(f"Cleaned {len(projects_to_clean)} project records")
        
        # Clean services
        services_to_clean = Service.query.filter(Service.title.like(f"%{problematic_text}%")).all()
        for service in services_to_clean:
            if problematic_text in service.title:
                service.title = service.title.replace(problematic_text, "").strip() or "Cleaned Service"
        print(f"Cleaned {len(services_to_clean)} service records")
        
        # Commit all changes
        db.session.commit()
        print("Database cleanup completed successfully!")

if __name__ == "__main__":
    clean_database()
