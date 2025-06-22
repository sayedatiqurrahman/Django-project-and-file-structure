from django import forms
from .models import AppVariety

class AppVarietiesForm(forms.Form):
    app_variety = forms.ModelChoiceField(
        queryset=AppVariety.objects.all(),
        label="App Variety",
    )