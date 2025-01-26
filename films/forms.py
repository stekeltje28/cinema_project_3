from django import forms
from .models import Location, Room, Film

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'address', 'city']  

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity', 'location']  

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'afbeelding', 'beschrijving', 'genre', 'min_leeftijd' ]