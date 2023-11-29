from django import forms
from myapp.models import Destinations


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destinations
        fields = ['Image', 'dname', 'eprice', 'description', 'country']

