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
    meetingID=models.ForeignKey("meetingID", on_delete=models.CASCADE)
    attendance=models.ManyToManyField(User)
    minutesText=models.TextField()

    class Meta:
        db_table="meeting_minutes"
        verbose_name_plural="meeting_minutes"

class Resource(models.Model):
    resourceName=models.CharField(max_length=255)
    resourceType=models.CharField(max_length=255)
    url=models.SlugField()
    dateEntered=models.DateTimeField()
    userID=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.CharField(max_length=255)

    class Meta:
        db_table="resource"
        verbose_name_plural="resources"

class Event(models.Model):
    eventTitle=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.DateTimeField()
    time=models.DateTimeField()
    description=models.TextField()
    userID=models.IntegerField()

    class Meta:
        db_table="event"
        verbose_name_plural="events"
