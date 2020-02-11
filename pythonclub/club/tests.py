from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

class MeetingTest(TestCase):
    def test_string(self):
        meetingTitle=Meeting(meetingTitle='Annual Meeting')
        meetingDate=Meeting(meetingDate='2020-06-23') 
        meetingTime=Meeting(meetingTime='03:30 PM')
        location=Meeting(location='Community Center')
        agenda=Meeting(agenda='Vote new board members')
        self.assertEqual(str(meetingTitle), meetingTitle.meetingTitle)
        self.assertEqual(str(meetingDate), meetingDate.meetingDate)
        self.assertEqual(str(meetingTime), meetingTime.meetingTime)
        self.assertEqual(str(location), location.location)
        self.assertEqual(str(agenda), agenda.agenda)

class MeetingMinutesTest(TestCase):
    def test_string(self):
        attendance=MeetingMinutes(attendance='Bob Boberton')
        minutesText=MeetingMinutes(minutesText='Susie Sue was voted in as board president')
        self.assertEqual(str(attendance), attendance.attendance)
        self.assertEqual(str(minutesText), minutesText.minutesText)

class ResourceTest(TestCase):
    def test_string(self):
        resourceName=Resource(resourceName='Offical Documentation')
        resourceType=Resource(resourceType='Django')
        url=Resource(url='https://docs.djangoproject.com/en/3.0/')
        dateEntered=Resource(dateEntered='2020-09-02')
        description=Resource(description='This is the offical documentation on Django')
        self.assertEqual(str(resourceName), resourceName.resourceName)
        self.assertEqual(str(resourceType), resourceType.resourceType)
        self.assertEqual(str(url), url.url)
        self.assertEqual(str(dateEntered), dateEntered.dateEntered)
        self.assertEqual(str(description), description.description)

class EventTest(TestCase):
    def test_string(self):
        eventTitle=Event(eventTitle='PyDay')
        location=Event(location='Programmers Ale House')
        date=Event(date='2020-02-21')
        time=Event(time='06:30 PM')
        description=Event(description='A day to celebrate Python!')
        self.assertEqual(str(eventTitle), eventTitle.eventTitle)
        self.assertEqual(str(location), location.location)
        self.assertEqual(str(date), date.date)
        self.assertEqual(str(time), time.time)
        self.assertEqual(str(description), description.description)




