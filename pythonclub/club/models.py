from django.db import models
from django.contrib.auth.models import User

class Meeting(models.Model):
    meetingTitle
    meetingDate
    meetingTime
    location
    agenda

    class Meta:
        db_table="meeting"
        verbose_name_plural="meetings"

class MeetingMinutes(models.Model):
    meetingID
    attendance
    minutesText

    class Meta:
        db_table="meetingminutes"
        verbose_name_plural="meetingminutes"

class Resource(models.Model):
    resourceName
    resourceType
    url
    dateEntered
    userID
    description

    class Meta:
        db_table="resource"
        verbose_name_plural="resources"

class Event(models.Model):
    eventTitle
    location
    date
    time
    description
    userID

    class Meta:
        db_table="event"
        verbose_name_plural="events"
