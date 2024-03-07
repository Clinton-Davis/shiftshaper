from django import forms
from .models import Roster


class RosterForm(forms.ModelForm):
    class Meta:
        model = Roster
        exclude = ["week"]  # Exclude the week field
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }
