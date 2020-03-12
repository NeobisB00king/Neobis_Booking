from django import forms

from .models import Images

class IndexForm(forms.Form):


    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField(
        max_length=100, required=True, label='Subject field')
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'cols': 70, 'class': 'form-control'}), required=True, label='Message field')

