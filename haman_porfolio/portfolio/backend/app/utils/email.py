import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import current_app
import os


def send_email(to_email, subject, body, is_html=False):
    """
    Send an email using SMTP
    """
    try:
        # Get SMTP configuration from environment variables
        smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
        smtp_port = int(os.environ.get('SMTP_PORT', 587))
        smtp_username = os.environ.get('SMTP_USERNAME', 'default@example.com')  # Using default email as fallback
        smtp_password = os.environ.get('SMTP_PASSWORD', '')  # Should be set in environment

        # Create message
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Add body to email
        if is_html:
            msg.attach(MIMEText(body, 'html'))
        else:
            msg.attach(MIMEText(body, 'plain'))

        # Create SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable security
        server.login(smtp_username, smtp_password)

        # Send email
        text = msg.as_string()
        server.sendmail(smtp_username, to_email, text)
        server.quit()

        return True
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False


def send_subscription_confirmation_email(email):
    """
    Send a subscription confirmation email
    """
    subject = "Welcome to Hamman Muraya's Newsletter!"
    body = f"""
    <html>
        <body>
            <h2>Welcome to Hamman Muraya's Newsletter!</h2>
            <p>Thank you for subscribing to my newsletter. You'll now receive updates on my latest projects, articles, and technical insights.</p>
            <p>Best regards,<br>Hamman Muraya</p>
        </body>
    </html>
    """
    return send_email(email, subject, body, is_html=True)


def send_contact_acknowledgment_email(name, email, message):
    """
    Send an acknowledgment email for contact form submissions
    """
    subject = "Acknowledgment: Your Message Has Been Received"
    body = f"""
    <html>
        <body>
            <h2>Thank You for Contacting Me!</h2>
            <p>Dear {name},</p>
            <p>This is an acknowledgment that I have received your message:</p>
            <p><strong>Message:</strong> {message}</p>
            <p>I will review your message and get back to you as soon as possible.</p>
            <p>Best regards,<br>Hamman Muraya</p>
        </body>
    </html>
    """
    return send_email(email, subject, body, is_html=True)


def send_resume_download_link(email, download_link):
    """
    Send an email with resume download link
    """
    subject = "Your Requested Resume Download Link"
    body = f"""
    <html>
        <body>
            <h2>Your Resume Download Link</h2>
            <p>Thank you for your interest in my resume.</p>
            <p>You can download my resume using the following link:</p>
            <p><a href="{download_link}">Download Resume</a></p>
            <p>Best regards,<br>Hamman Muraya</p>
        </body>
    </html>
    """
    return send_email(email, subject, body, is_html=True)