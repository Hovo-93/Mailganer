import os

from django.urls import reverse
from dotenv import load_dotenv
from sending_emails.smtp_client import SmtpClient
from email.mime.text import MIMEText
from django.template.loader import render_to_string


class MailSender:
    def __init__(self):
        self._sender = self._get_sender()

    def send(self, email):
        templateName = email.newsletter.template_name
        subscriber = email.subscriber
        template_path = "sending_emails/" + templateName
        html_body = render_to_string(template_path, self._get_user_context(subscriber))
        html_body = self._inject_pixel(html_body, email.id)
        msg = MIMEText(html_body, "html")
        msg["Subject"] = "Special for you"

        self._sender.send(subscriber.email, msg.as_string())

    def _get_sender(self):
        load_dotenv()
        sender = os.getenv('EMAIL_HOST_USER')
        password = os.getenv('EMAIL_HOST_PASSWORD')
        host = os.getenv('EMAIL_HOST')
        port = os.getenv('EMAIL_PORT')
        return SmtpClient(sender, password, host, port)

    def _get_user_context(self, subscriber):
        """
        Получение данных о подписчике
        :param subscriber:
        :return:
        """
        return {
            'name': subscriber.first_name,
            'last_name': subscriber.first_name,
            'birthday': subscriber.birthday
        }

    def _inject_pixel(self, html, email_id):
        """
            Отслеживание открытий писем (by attaching a small pixel image)
        :param html:
        :param email_id:
        :return:
        """
        url = reverse('tracker', kwargs={'id': email_id})
        image_html = '<img src="' + url + '">'
        print(image_html)
        return html.replace("<body>", image_html + "<body>")
