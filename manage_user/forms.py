from django import forms
from .models import User,Image

class Userforms(forms.ModelForm):
     class Meta:
         model=User
         fields = '__all__'

class ImageForms (forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


class Key_forms (forms.ModelForm):
    class Meta:
        model = User
        fields = ['key']



