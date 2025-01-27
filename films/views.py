
from django.shortcuts import render, get_object_or_404
from .models import Location, Room, Film
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from films.forms import FilmForm
from .forms import FilmForm, LocationForm
from films.models import Location, Room
from reserveringen.models import Event, Reservering


def location_list(request):
    locations = Location.objects.all()  
    messages.success(request, 'Het is gelukt!')
    return redirect('/accounts/dashboard')


def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)  
        if form.is_valid():
            form.save()  
            return redirect('/accounts/dashboard')
    else:
        form = LocationForm()  
    return redirect('/accounts/dashboard')


from .forms import RoomForm


def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room succesvol toegevoegd!')
            return redirect('dashboard')
    else:
        form = RoomForm()

    locations = Location.objects.all()

    return redirect('dashboard', {'locations': locations, 'form':form})
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    room.delete()

    messages.success(request, 'het is gelukt!')

    return redirect('/accounts/dashboard')


from django.shortcuts import get_object_or_404, redirect
from .models import Location


def delete_location(request, location_id):

    location = get_object_or_404(Location, id=location_id)

    location.delete()

    messages.success(request, 'het is gelukt!')


    return redirect('/accounts/dashboard')

from django.shortcuts import render, redirect

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()  
            messages.success(request, 'Film succesvol toegevoegd!')
            return redirect('/accounts/dashboard')  
        else:
            messages.error(request, 'Er is iets mis gegaan bij het toevoegen van de film!')
            return redirect('/accounts/films/add/')  
    else:

        return redirect('/accounts/dashboard')  

def film_detail(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    events = Event.objects.filter(film=film)

    context = {
        'film': film,
        'events': events,
    }
    return render(request, 'pages/film_detail.html', context)

def film_list(request):
    films = Film.objects.all()

    locatie_filter = request.GET.getlist('locatie[]')
    genre_filter = request.GET.get('genre')
    min_leeftijd_filter = request.GET.get('min_leeftijd')
    film_naam_filter = request.GET.get('film_naam')

    if locatie_filter:
        films = films.filter(events__location__name__in=locatie_filter)

    if genre_filter:
        films = films.filter(genre__iexact=genre_filter)

    if min_leeftijd_filter and min_leeftijd_filter.isdigit():
        films = films.filter(min_leeftijd__gte=int(min_leeftijd_filter))

    if film_naam_filter:
        films = films.filter(title__icontains=film_naam_filter)

    context = {
        'films': films,
        'locations': Location.objects.all(),
        'locatie_filter': locatie_filter,  
        'genre_filter': genre_filter,
        'film_naam_filter': film_naam_filter,
    }
    return render(request, 'pages/film_list.html', context)

