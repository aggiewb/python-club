from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('meeting/', views.getMeeting, name='meeting'), 
    path('meeting_minutes/', views.getMeetingMinutes, name='meeting_minutes'),
    path('resource/', views.getResource, name='resource'),
    path('event/', views.getEvent, name='event'),
]