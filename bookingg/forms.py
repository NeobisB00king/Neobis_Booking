import datetime

from django import forms
from django.forms import ModelForm

from .models import Room, Booking


class CreateRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class SearchRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class BookingForm(ModelForm):
    date_from = forms.DateField(initial=datetime.date.today)
    date_to = forms.DateField(initial=datetime.date.today)
    class Meta:
        model = Booking
        fields = [
            'date_from',
            'date_to',
            'comment',
            'has_child',
            'clientName',
            'clientSurname',
            'clientEmail',
            'clientPhone',
            ]
        labels = {
            'date_from': 'Date from which to book',
            'date_to': 'Date to which to book',
            'comment': 'If you have any prefrences write them here',
            'has_child': 'Check this if a child will be with you',
            'clientName': 'Your name',
            'clientSurname': 'Your surname',
            'clientEmail': 'Your email',
            'clientPhone': 'Your phone number',
        }
        widgets = {
            'date_from': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'date_to': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
