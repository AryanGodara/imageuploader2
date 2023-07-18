# forms.py

from django import forms
from django.forms import inlineformset_factory
from .models import Dataset, Image

# class DatasetForm(forms.ModelForm):
#     class Meta:
#         model = Dataset
#         fields = ['title', 'description', 'name']

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ['name', 'image']

# ImageFormSet = inlineformset_factory(Dataset, Image, form=ImageForm, extra=3)

class DatasetForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    title = forms.CharField(max_length=100)
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))