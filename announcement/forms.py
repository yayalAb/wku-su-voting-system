from django import forms
from .models import AnnounceModel


class AnnounceModelForms (forms.ModelForm):
    class Meta:
        model = AnnounceModel
        fields = '__all__'
