from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def meeting(request):
    meetings = Meeting.objects.all()
    return render(request, 'club/meeting.html', {'meeting' : meeting})

def meetingID(request, id):
    meetingID = get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingID.html', {'meetingID': meetingID})

def meetingMinutes(request):
    meetingMinutes = MeetingMinutes.objects.all()
    return render(request, 'club/meeting_minutes.html', {'meetingMinutes' : meetingMinutes})

def resource(request):
    resource = Resource.objects.all()
    return render(request, 'club/resource.html', {'resource' : resource})

def event(request):
    event = Event.objects.all()
    return render(request, 'club/event.html', {'event' : event}) 
