from django.shortcuts import render
from sending_emails.tasks import send_email
from email.mime.text import MIMEText
from sending_emails.models import User
from dotenv import load_dotenv
from django.template.loader import render_to_string
import smtplib
import os


def index(request):
    send_email.delay()
    # global html_body, to
    # load_dotenv()
    # users = User.objects.all()
    # # each_email = [user.email for user in users]
    # sender = os.getenv('EMAIL_HOST_USER')
    # password = os.getenv('EMAIL_HOST_PASSWORD')
    # server = smtplib.SMTP(os.getenv('EMAIL_HOST'), os.getenv('EMAIL_PORT'))
    # server.starttls()
    # server.login(sender, password)
    #
    # for user in users:
    #     to = user.email
    #     html_body = render_to_string('sending_emails/test.html', {'name': user.first_name})
    #     msg = MIMEText(html_body, "html")
    #     msg["Subject"] = "Special for you"
    #     server.sendmail(sender, to, msg.as_string())
    #     print(html_body)
    #
    #     # try:
    #     #     # msg = MIMEText(html_body, "html")
    return render(request, 'sending_emails/test.html')

    # except Exception as ex:
    #     return f"{ex}check your login or pass please!"
