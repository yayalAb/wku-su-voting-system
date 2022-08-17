from django.urls import path,include
from .views import Announce,UpdateAnnounce,Announcement,DeleteAnnounce,ManageAnnouncement




urlpatterns = [
    path('',Announcement,name="Announcement"),
    path('Announcements/',Announce,name="Announce"),
    path('UpdateAnnounce/<int:pk>/',UpdateAnnounce,name="UpdateAnnounce"),
    path('DeleteAnnounce/<int:pk>/',DeleteAnnounce,name="DeleteAnnounce"),
    path('ManageAnnouncement/',ManageAnnouncement,name="ManageAnnouncement"),
    ]