from django.forms import ModelForm
from django import forms
from polls.models import Memory


class DateInput(forms.DateInput):
    input_type = 'date'


class MemoryForm(ModelForm):
    class Meta:
        model = Memory
        fields = ["title", "comment", "date", "certificate"]
        widgets = {
            "date": DateInput(),
        }
