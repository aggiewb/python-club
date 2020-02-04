from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('meeting/', views.meeting, name='meeting'), 
    path('meeting_details/', views.meetingDetails, name='meeting_details'),
    path('resource/', views.resource, name='resource'),
    path('event/', views.event, name='event'),
]