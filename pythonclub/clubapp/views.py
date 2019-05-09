from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Event, Resource

# Create your views here.
def index (request):
    return render(request, 'clubapp/index.html')

def getinfo(request):
    resource_list=Resource.objects.all()
    return render(request, 'clubapp/resources.html', {'resource_list' : resource_list})   

def getmeetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'clubapp/meetings.html', {'meeting_list': meeting_list})

def meetingdetails(request, id):
    meet_detail=get_object_or_404(Meeting, pk=id)
    return render(request, 'clubapp/meetingdetails.html', {'meet_detail': meet_detail})
