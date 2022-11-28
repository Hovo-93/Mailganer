from sending_emails.views import index, tracker
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('tracking/<id>',tracker,name="tracker")
]
