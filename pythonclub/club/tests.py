from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse
from .views import index, meeting, meetingDetails, resource, event


class MeetingTest(TestCase):
    def test_string(self):
        meetingTitle=Meeting(meetingTitle='Annual Meeting')
        self.assertEqual(str(meetingTitle), meetingTitle.meetingTitle)

class MeetingMinutesTest(TestCase):
    def test_string(self):
        minutesText=MeetingMinutes(minutesText='Susie Sue was voted in as board president')
        self.assertEqual(str(minutesText), minutesText.minutesText)

class ResourceTest(TestCase):
    def test_string(self):
        resourceName=Resource(resourceName='Offical Documentation')
        self.assertEqual(str(resourceName), resourceName.resourceName)

class EventTest(TestCase):
    def test_string(self):
        eventTitle=Event(eventTitle='PyDay')
        self.assertEqual(str(eventTitle), eventTitle.eventTitle)
        
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)





