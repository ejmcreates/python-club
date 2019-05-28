from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .views import index, getinfo, getmeetings, meetingdetails
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import MeetingForm
import datetime

# Create your tests here.

class MeetingTest(TestCase):
    def test_string(self):
        meet=Meeting(meetingtitle="Python is Fun")
        self.assertEqual(str(meet), meet.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')    

class MeetingMinutesTest(TestCase):  
    def test_string(self):
        mint=MeetingMinutes(minutes="Python")
        self.assertEqual(str(mint), mint.minutes) 

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def test_string(self):
        source=Resource(resourcename="Python Tutorial")
        self.assertEqual(str(source), source.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_string(self):
        loc=Event(eventlocation="Coffee Shop")
        self.assertEqual(str(loc), loc.eventlocation)                

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

#testing views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)        

class GetInfoTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('info'))
        self.assertEqual(response.status_code, 200)    

class GetMeetingsTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)  

class GetMeetingDetailsTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetingdetails'))
        self.assertEqual(response.status_code, 200)  

class MeetingFormTest(TestCase):
    def test_meetingForm(self):
        info={
            'meetingtitle':"meeting1",
            'meetingdate': datetime.date(2019, 5, 28),
            'meetingtime':datetime.time(11, 00),
            'location':"library",
            'agenda':"talking bunches",
        }   
        form=MeetingForm(data=info)
        self.assertTrue(form.is_valid)

class MeetingFormTestInvalid(TestCase):
    def test_meetingForm(self):
        info={
            'meetingtitle':"meeting1",
            'meetingdate': datetime.date(2019, 5, 28),
            'meetingtime':datetime.time(11, 00),
            'location':"",
            'agenda':"talking bunches",
        }   
        form=MeetingForm(data=info)
        self.assertFalse(form.is_valid())
