from utils.email_helper import send_email

def alert_security(subject, report):
    send_email(subject, report)

