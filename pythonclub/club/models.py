from django.db import models
from django.contrib.auth.models import User

class Meeting(models.Model):
    meetingTitle=models.Charfield(max_length=255)
    meetingDate
    meetingTime
    location=models.Charfield(max_length=255)
    agenda=models.Charfield(max_length=255)

    class Meta:
        db_table="meeting"
        verbose_name_plural="meetings"

class MeetingMinutes(models.Model):
    meetingID
    attendance
    minutesText=models.TextField()

    class Meta:
        db_table="meetingminutes"
        verbose_name_plural="meetingminutes"

class Resource(models.Model):
    resourceName=models.Charfield(max_length=255)
    resourceType
    url
    dateEntered
    userID
    description=models.Charfield(max_length=255)

    class Meta:
        db_table="resource"
        verbose_name_plural="resources"

class Event(models.Model):
    eventTitle=models.Charfield(max_length=255)
    location
    date
    time
    description=models.TextField()
    userID

    class Meta:
        db_table="event"
        verbose_name_plural="events"
