from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns= [ 
	path('email_send/', views.email_send,name="email_send"),
	path('',TemplateView.as_view(template_name = 'index.html') ,name ='home')
]