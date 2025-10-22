from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template
from email_service import EmailService
import requests
from datetime import datetime
from dotenv import load_dotenv
import os


class JokeService:
    def __init__(self):
        load_dotenv()
        self.to_emails = os.getenv("TO_EMAILS")
        self.bcc_emails = os.getenv("BCC_EMAILS")
        self.cc_emails = os.getenv("CC_EMAILS")
        self.joke_api = "https://official-joke-api.appspot.com/jokes/random"
        self.email_service = EmailService()

    def fetch_joke(self):
        # TODO: fetch joke
        response = requests.get(self.joke_api)
        joke_dict = response.json()
        # print(joke_dict)
        return joke_dict

    def get_unique_dt_str(self):
        return datetime.now().strftime("%dth %b %Y at %H:%M:%S %p")

    def build_email_message(self, joke_dict):
        template = Template(Path("joke_template.html").read_text())
        body = template.substitute({"setup": joke_dict['setup'], "punchline": joke_dict['punchline']})

        message = MIMEMultipart()
        # message["Resent-Date", datetime.now()]
        message["from"] = "bijay.soren@gmail.com"
        message["to"] = self.to_emails
        message["cc"] = self.cc_emails
        message["bcc"] = self.bcc_emails
        message["subject"] = "Joke sent on " + self.get_unique_dt_str()
        message.attach(MIMEText(body, "html"))

        return message

    def send_joke(self):
        joke = self.fetch_joke()
        message = self.build_email_message(joke)
        self.email_service.send_email(message)


if __name__ == "__main__":
    js = JokeService()
    print(f'Sending emails to {js.to_emails}')
    js.send_joke()
    print(f'Joke sent successfully on {js.get_unique_dt_str()}')