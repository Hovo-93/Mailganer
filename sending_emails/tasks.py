from django.db.models import Q
from django.utils.timezone import now

from mailganer.celery import app
from sending_emails.mail_sender import MailSender
from sending_emails.models import Newsletter, Email


@app.task
def sender_task():
    emails_to_send = Email.objects.filter(status=Email.PENDING)
    mailSender = MailSender()
    for email in emails_to_send:
        try:
            mailSender.send(email)
            email.status = Email.SENT
        except Exception:
            email.status = Email.ERROR
        email.save()


@app.task
def schedule_checker():
    newsletters = Newsletter.objects.filter(status=Newsletter.SCHEDULED).filter(Q(scheduled_at__lte=now()))
    for newsletter in newsletters:
        newsletter.set_pending()
        subscribers = newsletter.subscribers.all()
        for sub in subscribers:
            Email.objects.create(
                status=Email.PENDING,
                newsletter_id=newsletter.id,
                subscriber_id=sub.id
            )

        newsletter.set_completed()
