import os
import smtplib
from email.mime.text import MIMEText
from mailganer.celery import app
from django.template.loader import render_to_string
from dotenv import load_dotenv

from sending_emails.models import User


@app.task
def send_email():
    load_dotenv()
    sender = os.getenv('EMAIL_HOST_USER')
    password = os.getenv('EMAIL_HOST_PASSWORD')
    server = smtplib.SMTP(os.getenv('EMAIL_HOST'), os.getenv('EMAIL_PORT'))
    server.starttls()
    server.login(sender, password)

    for user in User.objects.all():
        to = user.email
        html_body = render_to_string('sending_emails/test.html', {'name': user.first_name})
        msg = MIMEText(html_body, "html")
        msg["Subject"] = "Special for you"
        server.sendmail(sender, to, msg.as_string())
