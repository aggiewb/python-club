from django.db import models
from django.contrib.auth.models import User

class Meeting(models.Model):
    meetingTitle=models.CharField(max_length=255)
    meetingDate=models.DateField()
    meetingTime=models.TimeField()
    location=models.CharField(max_length=255)
    agenda=models.CharField(max_length=255)

    def __str__(self):
        return self.meetingTitle

    class Meta:
        db_table="meeting"
        verbose_name_plural="meetings"

class MeetingMinutes(models.Model):
    meetingID=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance=models.ManyToManyField(User)
    minutesText=models.TextField()

    def __str__(self):
         return self.minutesText

    class Meta:
        db_table="meeting_minutes"
        verbose_name_plural="meeting_minutes"

class Resource(models.Model):
    resourceName=models.CharField(max_length=255)
    resourceType=models.CharField(max_length=255)
    url=models.URLField()
    dateEntered=models.DateField()
    userID=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.CharField(max_length=255)

    def __str__(self):
         return self.resourceName

    class Meta:
        db_table="resource"
        verbose_name_plural="resources"

class Event(models.Model):
    eventTitle=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TimeField()
    description=models.TextField()
    userID=models.IntegerField()

    def __str__(self):
         return self.eventTitle

    class Meta:
        db_table="event"
        verbose_name_plural="events"
