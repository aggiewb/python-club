from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('meeting/', views.meeting, name='meeting'), 
    path('meeting_minutes/', views.meetingMinutes, name='meeting_minutes'),
    path('resource/', views.resource, name='resource'),
    path('event/', views.event, name='event'),
]