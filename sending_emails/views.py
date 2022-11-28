from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.timezone import now
from sending_emails.models import Email


def index(request):
    return render(request, 'sending_emails/index.html')


def tracker(request, id):
    email = Email.objects.filter(id=id).first()
    email.opened_at = now()
    email.save()

    img = open('static/pixel.gif', 'rb')

    return FileResponse(img)
