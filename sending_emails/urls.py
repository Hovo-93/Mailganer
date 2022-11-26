from sending_emails.views import index
from django.urls import path

urlpatterns = [
    path('', index, name='send_email'),
]
