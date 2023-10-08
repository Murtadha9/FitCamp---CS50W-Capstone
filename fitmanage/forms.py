from django import forms
from .models import AddMember ,WeeklyReport

class memberForm(forms.ModelForm):
    class Meta:
        model = AddMember
        fields = '__all__'

        



class WeeklyReportForm(forms.ModelForm):
    class Meta:
        model = WeeklyReport
        fields = ['title', 'content']        