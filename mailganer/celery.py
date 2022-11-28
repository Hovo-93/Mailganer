"""
Файл настроек Celery
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
"""
from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
import django

# этот код скопирован с manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailganer.settings')
django.setup()

# здесь вы меняете имя
app = Celery("mailganer")

# Для получения настроек Django, связываем префикс "CELERY" с настройкой celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# загрузка tasks.py в приложение django
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-scheduled-newsletters': {
        'task': 'sending_emails.tasks.schedule_checker',
        'schedule': crontab(minute='*/1')
    },
    'send-pending-newsletters': {
        'task': 'sending_emails.tasks.sender_task',
        'schedule': crontab(minute='*/1')
    },
}
