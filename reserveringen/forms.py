from django import forms
from .models import Reservering, Event

class ReserveringForm(forms.ModelForm):
    class Meta:
        model = Reservering
        fields = ['gebruiker','aantal_tickets', 'status']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['film', 'location', 'room', 'date', 'totaal_aantal_plekken']
