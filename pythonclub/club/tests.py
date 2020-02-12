from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse
from .views import index, meeting, meetingDetails, resource, event


class MeetingTest(TestCase):
    def test_string(self):
        meetingTitle=Meeting(meetingTitle='Annual Meeting')
        self.assertEqual(str(meetingTitle), meetingTitle.meetingTitle)
    
    def setUp(self):
       meeting=Meeting(agenda='Voting on new club board members', location='Community Center', meetingDate='2020-06-23', meetingTime='03:00 pm')
       return meeting
    
    def test_type(self):
        meeting = self.setUp()
        self.assertEqual(str(meeting.agenda), 'Voting on new club board members')
    
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def test_string(self):
        minutesText=MeetingMinutes(minutesText='Susie Sue was voted in as board president')
        self.assertEqual(str(minutesText), minutesText.minutesText)
    
    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meeting_minutes')

class ResourceTest(TestCase):
    def test_string(self):
        resourceName=Resource(resourceName='Offical Documentation')
        self.assertEqual(str(resourceName), resourceName.resourceName)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_string(self):
        eventTitle=Event(eventTitle='PyDay')
        self.assertEqual(str(eventTitle), eventTitle.eventTitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')


class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class ResourceViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resource'))
        self.assertEqual(response.status_code, 200)





