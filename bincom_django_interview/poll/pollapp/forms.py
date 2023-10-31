from django import forms 

from .models import lga

class LgaResultForm(forms.Form):
    lga = forms.ModelChoiceField(queryset=lga.objects.all())


