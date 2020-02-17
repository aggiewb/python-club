from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, MeetingMinutesForm

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def meeting(request):
    meeting = Meeting.objects.all()
    return render(request, 'club/meeting.html', {'meeting' : meeting})

def meetingDetails(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    meetingMinutes = MeetingMinutes.objects.filter(meetingID=id)
    return render(request, 'club/meeting_details.html', context={'meeting' : meeting, 'meetingMinutes' : meetingMinutes,})

def resource(request):
    resource = Resource.objects.all()
    return render(request, 'club/resource.html', {'resource' : resource})

def event(request):
    event = Event.objects.all()
    return render(request, 'club/event.html', {'event' : event})

def newMeeting(request):
    meeting_form=MeetingForm
    minutes_form=MeetingMinutesForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            meeting_form=MeetingForm()
            minutes_form=MeetingMinutesForm()
    else:
        meeting_form=MeetingForm()
        minutes_form=MeetingMinutesForm()
    return render(request, 'club/newmeeting.html', {'meeting_form': meeting_form, 'minutes_form': minutes_form})
