from django import forms
from .models import Schedule

class ScheduleForm (forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('year','month','day','time','task','details','importance')
