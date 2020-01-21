from django.db import models
from django.contrib.auth.models import User

class Meeting(models.Model):
    class Meta:
        db_table="meeting"
        verbose_name_plural="meetings"

class MeetingMinutes(models.Model):
    class Meta:
        db_table="meetingminutes"
        verbose_name_plural="meetingminutes"

class Resource(models.Model):
    class Meta:
        db_table="resource"
        verbose_name_plural="resources"

class Event(models.Model):
    class Meta:
        db_table="event"
        verbose_name_plural="events"
