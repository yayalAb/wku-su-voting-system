from django import forms
from .models import exam_model


class ExamForms (forms.ModelForm):
    class Meta:
        model = exam_model
        fields = ['question','choiceA',  'choiceB', 'choiceC',   'choiceD',  'choiceE', 'answer']
class AnsForms (forms.ModelForm):
    class Meta:
        model = exam_model
        fields = ['User_answer']

