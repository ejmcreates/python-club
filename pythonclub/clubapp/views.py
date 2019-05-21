from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Event, Resource
from .forms import ResourceForm, MeetingForm
from django.contrib.auth.decorators import login_required

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

@login_required
def newResource(request):
    form=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'clubapp/newresource.html', {'form': form})            

@login_required
def newMeeting(request):
    form=MeetingForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'clubapp/newmeeting.html', {'form': form})

def loginmessage(request):
    return render(request, 'clubapp/loginmessage.html')    

def logoutmessage(request):
    return render(request, 'clubapp/logoutmessage.html')
