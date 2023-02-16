from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
def email_send(request):
	if request.POST:
		email = request.POST.get('email')
		name =   request.POST.get('name')
		message =  request.POST.get('message')
		template = render_to_string('email.html', {
			'name' :name,
			'email': email,
			'message': message




			})
		message =EmailMessage('portfolio',template,settings.EMAIL_HOST_USER,['senchuknazar6@gmail.com'])
		message.fail_silently = False
		message.send()
		return HttpResponse('Email was sent!')