from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getMeeting/', views.getMeeting, name='meeting'), 
    path{'getMeetingMinutes/', views.getMeetingMinutes, name='meeting_minutes'},
    path{'getResource/', views.getResource, name='resource'},
    path{'getEvent', views.getEvent, name='event'},
]