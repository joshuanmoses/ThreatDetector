import smtplib
from email.mime.text import MIMEText
from config import settings

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = settings.EMAIL_USERNAME
    msg['To'] = ", ".join(settings.ALERT_RECIPIENTS)
    
    with smtplib.SMTP(settings.EMAIL_SMTP_SERVER, settings.EMAIL_PORT) as server:
        server.starttls()
        server.login(settings.EMAIL_USERNAME, settings.EMAIL_PASSWORD)
        server.sendmail(settings.EMAIL_USERNAME, settings.ALERT_RECIPIENTS, msg.as_string())
