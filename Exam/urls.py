from django.urls import path,include
from .views import AddExamQst,Exams,DeleteExams,Exams1,UpdateQuestions,Questions,DeleteQuestion




urlpatterns = [
    path('AddExamQst',AddExamQst,name="AddExamQst"),
    path('Exams/',Exams1,name="Exams"),
    path('Exams/<int:num>/<int:res>',Exams,name="Exams"),
    path('DeleteExams',DeleteExams,name="DeleteExams"),
    path('Questions',Questions,name="Questions"),
    path('UpdateQuestions/<int:pk>',UpdateQuestions,name="UpdateQuestions"),
    path ('DeleteQuestion/<int:pk>', DeleteQuestion, name="DeleteQuestion"),
    ]