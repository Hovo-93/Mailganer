from django.contrib import admin

from sending_emails.models import Subscriber, Newsletter, Email


# Register your models here.
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('template_name', 'scheduled_at', 'status', 'id', 'get_subscribers')

    filter_horizontal = ('subscribers',)

    def get_subscribers(self, obj):
        return [sub for sub in obj.subscribers.all()]


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday', 'email',)


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscriber', 'newsletter', 'status', 'opened_at')
