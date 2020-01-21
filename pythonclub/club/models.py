from django.db import models
from django.contrib.auth.models import User

class Meeting(models.Model):
    meetingTitle=models.CharField(max_length=255)
    meetingDate=models.DateTimeField()
    meetingTime=models.DateTimeField()
    location=models.CharField(max_length=255)
    agenda=models.CharField(max_length=255)

    class Meta:
        db_table="meeting"
        verbose_name_plural="meetings"

class MeetingMinutes(models.Model):
    meetingID
    attendance
    minutesText=models.TextField()

    class Meta:
        db_table="meeting_minutes"
        verbose_name_plural="meeting_minutes"

class Resource(models.Model):
    resourceName=models.CharField(max_length=255)
    resourceType
    url
    dateEntered=models.TimeDateField()
    userID
    description=models.CharField(max_length=255)

    class Meta:
        db_table="resource"
        verbose_name_plural="resources"

class Event(models.Model):
    eventTitle=models.CharField(max_length=255)
    location
    date=models.TimeDateField()
    time=models.TimeDateField()
    description=models.TextField()
    userID

    class Meta:
        db_table="event"
        verbose_name_plural="events"
