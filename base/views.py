from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
def email_send(request):
	return render(request,"email_send.html")