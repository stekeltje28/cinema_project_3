from django.contrib import admin
from .models import Film, Location, Room

from django.contrib import admin
from .models import Film
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'genre', 'min_leeftijd']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'id')
    search_fields = ('name', 'city', 'id')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'capacity', 'id')
    search_fields = ('name', 'location__name', 'id')
