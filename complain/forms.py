from django import forms
from .models import ComplainModel,Responsemodel


class ComplainForms (forms.ModelForm):
    class Meta:
        model = ComplainModel
        fields = '__all__'

class ResponseForms (forms.ModelForm):
    class Meta:
        model = Responsemodel
        fields = '__all__'
