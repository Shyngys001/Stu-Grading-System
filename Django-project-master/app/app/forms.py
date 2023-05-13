from django import forms
# noinspection PyUnresolvedReferences
from login.models import Subject


class AddGrade(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb2'}))
    student = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb2'}))
    professor = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb2'}))
    grade = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control mb2'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control mb2'}))
    observations = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb2'}))

    class Meta:
        model = Subject
        fields = ["name", "student", "professor", "grade", "date", "observations"]
