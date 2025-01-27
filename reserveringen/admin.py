from django.contrib import admin
from .models import Reservering, Event

@admin.register(Reservering)
class ReserveringAdmin(admin.ModelAdmin):
    list_display = ('gebruiker', 'aantal_tickets', 'status', 'reserveringsdatum', 'event')
    list_filter = ('status', 'reserveringsdatum')
    search_fields = ('gebruiker__email', 'film__title')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('film', 'location', 'room', 'date', 'totaal_aantal_plekken', 'id')
    list_filter = ('film', 'location', 'room', 'id')
    search_fields = ('film__title', 'location__name', 'room__name', 'id')
    date_hierarchy = 'date'  

