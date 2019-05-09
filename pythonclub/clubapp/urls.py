from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getinfo/', views.getinfo, name='info'),
    path('getmeetings/', views.getmeetings, name='meetings'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),

]
