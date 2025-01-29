from django.utils.timezone import now
from django.db import models

class Location(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100)  
    address = models.CharField(max_length=255, null=True, blank=True)  
    city = models.CharField(max_length=100, null=True, blank=True)  

    def __str__(self):
        return self.name

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="rooms")  
    name = models.CharField(max_length=100)  
    capacity = models.IntegerField()  

    def __str__(self):
        return f"{self.name} - {self.location.name}"

from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateTimeField(default=now)
    afbeelding = models.ImageField(upload_to='films/', null=True, blank=True)
    beschrijving = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=100)
    min_leeftijd = models.IntegerField()
    rooms = models.ManyToManyField(Room, related_name="films", blank=True)  

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Films"

    def __str__(self):
        return self.title


