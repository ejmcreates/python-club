from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Event, Resource

# Create your views here.
def index (request):
    return render(request, 'clubapp/index.html')

def getinfo(request):
    resource_list=Resource.objects.all()
    return render(request, 'clubapp/resources.html', {'resource_list' : resource_list})    