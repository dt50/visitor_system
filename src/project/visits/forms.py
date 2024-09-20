from django import forms
from .models import TimeVisits


class TimeVisitsForm(forms.ModelForm):
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    class Meta:
        model = TimeVisits
        fields = ("date", "time")
