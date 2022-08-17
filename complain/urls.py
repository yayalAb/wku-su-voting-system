from django.urls import path,include
from .views import complains,complain,UpdateComplain,DeleteComplain,Respose,Responses




urlpatterns = [
    path('',complain,name="complain"),
    path('complains/',complains,name="complains"),
    path('UpdateComplain/<int:pk>/',UpdateComplain,name="UpdateComplain"),
    path('DeleteComplain/<int:pk>/',DeleteComplain,name="DeleteComplain"),
    path('Respose/<int:pk>',Respose,name="Respose"),
    path('Responses/',Responses,name="Responses"),
    ]