from django.db import models
from django.conf import settings
from films.models import Film, Location, Room
from django.utils.timezone import now



class Reservering(models.Model):
    id = models.AutoField(primary_key=True)
    gebruiker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reserveringen'
    )
    event = models.ForeignKey(
        'event',
        on_delete=models.CASCADE,
        related_name='reserveringen',
    )
    aantal_tickets = models.PositiveIntegerField()
    reserveringsdatum = models.DateTimeField(auto_now_add=True)  
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'In behandeling'),
            ('confirmed', 'Bevestigd'),
            ('cancelled', 'Geannuleerd')
        ],
        default='pending'
    )  

    def __str__(self):

        return f"Reservering door {self.gebruiker.email} voor {self.event.film.title} ({self.aantal_tickets} tickets)"

class Event(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="events")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)  
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  
    date = models.DateTimeField()  
    totaal_aantal_plekken = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.film.title} - {self.location.name} - {self.date}"
