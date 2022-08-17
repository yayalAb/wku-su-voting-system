from django.urls import path
from .views import Home,mission,vision,contactUs

urlpatterns = [
    path('',Home,name="Home"),
    path('mission',mission,name="mission"),
    path('vision',vision,name="vision"),
    path('contactUs',contactUs,name="contactUs"),
    ]
