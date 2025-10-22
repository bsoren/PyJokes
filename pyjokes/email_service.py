import smtplib
from dotenv import load_dotenv
import os

class EmailService:
    def __init__(self):
        load_dotenv()
        self.email_user = os.getenv("EMAIL_USER")
        self.email_pass = os.getenv("EMAIL_PASS")

    def send_email(self, message):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(self.email_user, self.email_pass)
            smtp.send_message(message)
