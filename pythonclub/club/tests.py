from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

class MeetingTest(TestCase):
    def test_string(self):
        meetingTitle=Meeting(meetingTitle="Annual Meeting")
        meetingDate=Meeting(meetingDate="2020-06-23") 
        meetingTime=Meeting(meetingTime="03:30 PM")
        location=Meeting(location="Community Center")
        agenda=Meeting(agenda="Vote new board members")
        self.assertEqual(str(meetingTitle), meetingTitle.meetingTitle)
        self.assertEqual(str(meetingDate), meetingDate.meetingDate)
        self.assertEqual(str(meetingTime), meetingTime.meetingTime)
        self.assertEqual(str(location), location.location)
        self.assertEqual(str(agenda), agenda.agenda)

