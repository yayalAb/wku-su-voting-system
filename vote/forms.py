from django import forms
from .models import VotingModel


class VotingForms (forms.ModelForm):
    class Meta:
        model = VotingModel
        fields = ['username','protocol','presentation_skill', 'confidence','strategic_plane','answering','Time_management']
        #widgets = {'username': forms.CharField(attr='class'), 'protocol': 'DateInput'}

class EvaluationForms (forms.ModelForm):
    class Meta:
        model = VotingModel
        fields = ['username','certifcate','written_exam','oral_interview','Str_and_opra_plane']


