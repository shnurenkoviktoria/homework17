from django.forms import ModelForm

from polls.models import Memory


class MemoryForm(ModelForm):
    class Meta:
        model = Memory
        fields = ["title", "comment", "date", "certificate"]