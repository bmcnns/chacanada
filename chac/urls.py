from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<str:post_title>/detail', views.detail, name='detail'),
	path('schedule', views.schedule, name='schedule'),
	path('travel', views.travel, name='travel'),
	path('register', views.register, name='register'),
	path('volunteer', views.volunteer, name='volunteer'),
	path('contact', views.contact, name='contact'),
	path('manual', views.manual_register, name='manual_register'),
	path('thanks', views.thanks, name='thanks')
]
