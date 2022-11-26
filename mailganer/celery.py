"""
Файл настроек Celery
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
"""
from __future__ import absolute_import


import os
import smtplib
from email.mime.text import MIMEText

from celery import Celery

# этот код скопирован с manage.py
# он установит модуль настроек по умолчанию Django для приложения 'celery'.
from django.template.loader import render_to_string
from dotenv import load_dotenv
from celery.schedules import crontab

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailganer.settings')
django.setup()

from sending_emails.models import User

# здесь вы меняете имя
app = Celery("mailganer")

# Для получения настроек Django, связываем префикс "CELERY" с настройкой celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# загрузка tasks.py в приложение django
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sending-emails-every-two-minute': {
        'task': 'sending_emails.tasks.send_email',
        'schedule': crontab(minute='*/2')
    },
}

