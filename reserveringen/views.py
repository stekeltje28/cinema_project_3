from django.shortcuts import render, redirect
from .models import Reservering
from .forms import ReserveringForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from reserveringen.models import Event
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Film, Location, Room, Event
from django.http import HttpResponseBadRequest
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Film, Location, Room, Event
from datetime import datetime
from django.utils.timezone import make_aware

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.timezone import make_aware
from datetime import datetime
from django.core.exceptions import ValidationError
from films.models import Film, Location, Room

from django.shortcuts import render, redirect
from .models import Reservering
from django.contrib.auth.decorators import login_required


@login_required
def reservering(request, film_id):
    if request.method == 'POST':

        event_id = request.POST['event']
        aantal_tickets = int(request.POST['aantal'])

        event = get_object_or_404(Event, id=event_id)

        if event.totaal_aantal_plekken >= aantal_tickets:

            reservering = Reservering.objects.create(
                gebruiker=request.user,
                event=event,
                aantal_tickets=aantal_tickets
            )

            event.totaal_aantal_plekken -= aantal_tickets
            event.save()

            messages.success(request,
                             f'Reservering succesvol! Je hebt {aantal_tickets} tickets voor {event.film.title}.')

        else:

            messages.error(request, f'Helaas, er zijn niet genoeg plekken beschikbaar voor {aantal_tickets} tickets.')

        return redirect('film_detail', film_id=film_id)


@login_required
def update_reservering(request, reservering_id):
    reservering = Reservering.objects.get(id=reservering_id)

    if request.method == "POST":
        aantal_tickets = request.POST.get("aantal_tickets")
        if aantal_tickets.isdigit() and int(aantal_tickets) > 0:
            reservering.aantal_tickets = int(aantal_tickets)
            reservering.save()
            return redirect('/accounts/dashboard')

    return render(request, '/accounts/dashboard/', {'error': 'Ongeldig aantal tickets'})


@login_required
def delete_reservation(request, reservering_id):
    reservering = get_object_or_404(Reservering, id=reservering_id)

    if reservering.gebruiker == request.user:

        event = reservering.event
        event.totaal_aantal_plekken += reservering.aantal_tickets
        event.save()

        reservering.delete()

        messages.success(request, 'Reservering succesvol geannuleerd.')

    else:

        messages.error(request, 'Je kunt deze reservering niet annuleren.')

    return redirect('/accounts/dashboard/')


def assign_film_date_location(request):

    if request.method == "POST":
        film_id = request.POST.get('film')
        location_id = request.POST.get('location')
        room_id = request.POST.get('room')  # Correcte naam  # Correct gebruik: room in je formulier!
        datum_list = request.POST.getlist('datum[]')
        tijd_list = request.POST.getlist('tijd[]')
        beschikbare_plaatsen_id = request.POST.get('beschikbare_plaatsen')

        print("Film ID:", film_id)
        print("Location ID:", location_id)
        print("Room ID:", room_id)
        print("Datum List:", datum_list)
        print("Tijd List:", tijd_list)
        print("Beschikbare Plaatsen ID:", beschikbare_plaatsen_id)

        if not film_id or not location_id or not room_id or not datum_list or not tijd_list:
            messages.error(request, "Alle velden zijn verplicht.")
            return redirect('dashboard')

        try:
            beschikbare_plaatsen = int(beschikbare_plaatsen_id)
        except ValueError:
            messages.error(request, "Aantal beschikbare plaatsen moet een geldig getal zijn.")
            return redirect('dashboard')

        film = get_object_or_404(Film, id=film_id)
        location = get_object_or_404(Location, id=location_id)
        room = get_object_or_404(Room, id=room_id)

        if room.location != location:
            messages.error(request, "De geselecteerde zaal hoort niet bij de geselecteerde locatie.")
            return redirect('dashboard')

        success_count = 0
        failure_count = 0
        for datum, tijd in zip(datum_list, tijd_list):
            try:
                combined_datetime = datetime.strptime(f"{datum} {tijd}", "%Y-%m-%d %H:%M")
                combined_datetime = make_aware(combined_datetime)

                event = Event.objects.create(
                    film=film,
                    location=location,
                    room=room,
                    date=combined_datetime,
                    totaal_aantal_plekken=beschikbare_plaatsen
                )
                print("Event aangemaakt:", event)

                success_count += 1
            except Exception as e:
                failure_count += 1
                messages.error(request, f"Fout bij {datum} {tijd}: {str(e)}")

        if success_count > 0:
            messages.success(request, f"{success_count} evenementen succesvol aangemaakt.")
        if failure_count > 0:
            messages.error(request, f"{failure_count} evenementen konden niet worden aangemaakt.")
        return redirect('dashboard')

    films = Film.objects.all()
    locations = Location.objects.all()
    rooms = Room.objects.all()
    return render(request, 'accounts/dashboard.html', {
        'films': films,
        'locations': locations,
        'rooms': rooms
    })


from django.shortcuts import render, get_object_or_404
from .models import Event

from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Film, Location, Room
from .forms import EventForm

from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventForm
from .models import Event, Film, Location, Room
from datetime import time

from datetime import datetime


def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    films = Film.objects.all()
    locations = Location.objects.all()
    rooms = Room.objects.filter(location=event.location)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():

            datum_str = request.POST.get('date')
            tijd_str = request.POST.get('tijd')

            if datum_str and tijd_str:
                datum_tijd_str = f"{datum_str} {tijd_str}"
                event.date = datetime.strptime(datum_tijd_str, '%Y-%m-%d %H:%M')

            form.save()
            return redirect('dashboard')
    else:
        form = EventForm(instance=event)

    return render(request, 'pages/user_pages/edit_event.html', {
        'form': form,
        'films': films,
        'locations': locations,
        'rooms': rooms,
        'event': event
    })


def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        film_id = request.POST.get('film')
        location_id = request.POST.get('location')
        room_id = request.POST.get('zaal')
        datum = request.POST.get('datum')
        tijd = request.POST.get('tijd')
        totaal_aantal_plekken = request.POST.get('totaal_aantal_plekken')

        film = Film.objects.get(id=film_id)
        location = Location.objects.get(id=location_id)
        room = Room.objects.get(id=room_id)

        event.film = film
        event.location = location
        event.room = room
        event.date = datum
        event.time = tijd
        event.totaal_aantal_plekken = totaal_aantal_plekken

        event.save()

        return redirect('/account/dashboard',
                        event_id=event.id)

    return render(request, '/account/dashboard', {
        'event': event,
        'films': Film.objects.all(),
        'locations': Location.objects.all(),
    })
