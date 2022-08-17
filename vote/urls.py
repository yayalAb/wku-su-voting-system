from django.urls import path,include
from .views import Voting, Evaluate, changeStatus, fingerprint, ViewResult, ViewResult40, ViewResult60

urlpatterns = [
    path('Voting/<str:username>',Voting,name="Voting"),
    path ('Evaluate/<str:username>', Evaluate, name="Evaluate"),
    path('vtr/',changeStatus, name="vtr"),
    path('fingerprint/',fingerprint, name="fingerprint"),
    path ('ViewResult/', ViewResult, name="ViewResult"),
    path ('ViewResult40/', ViewResult40, name="ViewResult40"),
    path ('ViewResult60/', ViewResult60, name="ViewResult60"),
]