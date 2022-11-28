import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    birthday = models.DateField(verbose_name='дата рождения', null=True)


class Subscriber(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=150, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150, blank=True)
    email = models.EmailField(verbose_name='Емайл', blank=False)
    birthday = models.DateField(verbose_name='Дата рождения', null=True)

    def __str__(self):
        return f'{self.first_name}'


class Newsletter(models.Model):
    PENDING = 1
    SCHEDULED = 2
    STARTED = 3
    COMPLETED = 4
    STATUSES = (
        (PENDING, 'Pending'),
        (SCHEDULED, 'Scheduled'),
        (STARTED, 'Started'),
        (COMPLETED, 'Completed mail generation'),
    )
    template_name = models.CharField(verbose_name='Название шаблона', max_length=150)
    scheduled_at = models.DateTimeField(verbose_name='Время отправки', null=True)
    status = models.IntegerField(verbose_name='Статус', choices=STATUSES, default=PENDING)
    subscribers = models.ManyToManyField(Subscriber, related_name='newsletters')

    def __str__(self):
        return f'{self.template_name}'

    def set_started(self):
        self._update_status(self.STARTED)

    def set_pending(self):
        self._update_status(self.PENDING)

    def set_completed(self):
        self._update_status(self.COMPLETED)

    def _update_status(self, status):
        self.status = status
        self.save()


class Email(models.Model):
    PENDING = 1
    SENT = 2
    ERROR = 3
    STATUSES = (
        (PENDING, 'Pending'),
        (SENT, 'Sent'),
        (ERROR, 'Error'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    newsletter = models.ForeignKey(Newsletter, related_name='newsletter', on_delete=models.DO_NOTHING)
    subscriber = models.ForeignKey(Subscriber, related_name='subscriber', on_delete=models.DO_NOTHING)
    opened_at = models.DateTimeField(null=True, verbose_name='Время открытия')
    status = models.IntegerField(choices=STATUSES, default=PENDING, verbose_name='Статус')
