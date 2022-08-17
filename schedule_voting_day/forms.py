from django import forms
from .models import ScheduleModel

class DateInput(forms.DateInput):
    input_type = 'date'




class ScheduleForms (forms.ModelForm):
    class Meta:
        widgets={'Start_date':DateInput, 'End_date':DateInput}
        model = ScheduleModel
        fields = '__all__'
