from django import forms
from .models import Schedule

class ScheduleForm (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_id'].widget = forms.HiddenInput()
    class Meta:
        model = Schedule
        fields = ('year','month','day','time','task','details','category','importance','user_id')
