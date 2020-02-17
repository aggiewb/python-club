from django import forms
from .models import Meeting, MeetingMinutes, Resource, Event

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'
        model=MeetingMinutes
        fields= ['attendance', 'minutesText']