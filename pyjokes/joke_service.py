from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template
from email_service import EmailService
import requests
from datetime import datetime


class JokeService:
    def __init__(self):
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

    def build_email_message(self, to_emails, joke_dict):
        template = Template(Path("joke_template.html").read_text())
        body = template.substitute({"setup": joke_dict['setup'], "punchline": joke_dict['punchline']})

        message = MIMEMultipart()
        # message["Resent-Date", datetime.now()]
        message["from"] = "bijay.soren@gmail.com"
        message["to"] = to_emails
        message["bcc"] = "jhopro10@gmail.com"
        message["subject"] = "Joke sent on " + self.get_unique_dt_str()
        message.attach(MIMEText(body, "html"))

        return message

    def send_joke(self, to_emails):
        joke = self.fetch_joke()
        message = self.build_email_message(to_emails, joke)
        self.email_service.send_email(message)


if __name__ == "__main__":
    js = JokeService()
    emails = ["gr8mind42@gmail.com"]
    to_emails_str = ", ".join(emails)
    print(f'Sending emails to {to_emails_str}')
    js.send_joke(to_emails_str)
    print(f'Joke sent successfully on {js.get_unique_dt_str()}')