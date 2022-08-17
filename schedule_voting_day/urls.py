from django.urls import path,include
from .views import Schedule,Schedules,UpdateSchedule,DeleteSchedule




urlpatterns = [
    path('',Schedule,name="Schedule"),
    path('Schedules/',Schedules,name="Schedules"),
    path('UpdateSchedule/<int:pk>/',UpdateSchedule,name="UpdateSchedule"),
    path('DeleteSchedule/<int:pk>/',DeleteSchedule,name="DeleteSchedule"),
    ]