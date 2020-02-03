from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def meeting(request):
    type_list = Meeting.objects.all()
    return render(request, 'club/meeting.html', {'type_list' : type_list})

def meetingMinutes(request):
    type_list = MeetingMinutes.objects.all()
    return render(request, 'club/meeting_minutes.html', {'type_list' : type_list})

def resource(request):
    type_list = Resource.objects.all()
    return render(request, 'club/resource.html', {'type_list' : type_list})

def event(request):
    type_list = Event.objects.all()
    return render(request, 'club/event.html', {'type_list' : type_list}) 
