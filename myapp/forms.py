# forms.py

from django import forms
from django.forms import inlineformset_factory
from .models import Dataset, Image

class DatasetForm(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control '}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': "form-control"}))

