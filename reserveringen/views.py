from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.timezone import make_aware

from .models import Reservering



def reservering(request, film_id):
    if request.user.is_authenticated != True:
        return redirect(f'/films/{film_id}/?openLoginModal=1')

    elif request.method == 'POST':

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



def update_reservering(request, reservering_id):
    reservering = Reservering.objects.get(id=reservering_id)

    if request.method == "POST":
        aantal_tickets = request.POST.get("aantal_tickets")
        if aantal_tickets.isdigit() and int(aantal_tickets) > 0:
            reservering.aantal_tickets = int(aantal_tickets)
            reservering.save()
            return redirect('/accounts/dashboard')

    return render(request, '/accounts/dashboard/', {'error': 'Ongeldig aantal tickets'})

def edit_reservation(request, reservation_id):
    reservation = Reservering.objects.get(id=reservation_id)

    if request.method == 'POST':
        new_aantal_tickets = request.POST.get('aantal_tickets')
        print(new_aantal_tickets)


        if new_aantal_tickets:
            reservation.aantal_tickets = new_aantal_tickets
            reservation.save()
            return redirect('dashboard')

    return redirect('dashboard')


def delete_reservation(request, reservation_id):
    reservering = get_object_or_404(Reservering, id=reservation_id)

    print(reservering.id)
    reservering.delete()
    messages.success(request, 'Reservering succesvol verwijderd.')
    return redirect('/accounts/dashboard/')

def assign_film_date_location(request):
    if request.method == "POST":
        film_id = request.POST.get('film')
        location_id = request.POST.get('location')
        room_id = request.POST.get('room')  # Correcte naam  # Correct gebruik: room in je formulier!
        datum_list = request.POST.getlist('datum[]')
        tijd_list = request.POST.getlist('tijd[]')
        beschikbare_plaatsen_id = request.POST.get('beschikbare_plaatsen')

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

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    films = Film.objects.all()
    locations = Location.objects.all()
    rooms = Room.objects.filter(location=event.location)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)

        if form.is_valid():
            date_str = request.POST.get('date')
            time_str = request.POST.get('tijd')

            if date_str and time_str:
                try:
                    # Combineer de datum en tijd naar een datetime object
                    datetime_str = f"{date_str} {time_str}"
                    event_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
                    event.date = event_datetime  # Bewaar de gecombineerde datetime
                    form.save()  # Sla het event op
                    return redirect('dashboard')  # Of een andere URL waar je naartoe wilt na het opslaan
                except ValueError:
                    form.add_error(None, 'Datum of tijd is ongeldig')
            else:
                form.add_error(None, 'Datum en tijd zijn vereist.')

        else:
            return render(request, 'pages/user_pages/edit_event.html', {
                'form': form,
                'films': films,
                'locations': locations,
                'rooms': rooms,
                'event': event,
            })

    else:
        form = EventForm(instance=event)

    return render(request, 'pages/user_pages/edit_event.html', {
        'form': form,
        'films': films,
        'locations': locations,
        'rooms': rooms,
        'event': event
    })

from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from .models import Event, Film, Location, Room
from .forms import EventForm


def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)

        datum = request.POST.get('date')
        tijd = request.POST.get('tijd')

        if datum and tijd:
            datetime_str = f"{datum} {tijd}"
            try:
                event_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
                event.date = event_datetime  # Bewaar de gecombineerde datetime
            except ValueError:
                return render(request, 'account/edit_event.html', {
                    'form': form,
                    'error': 'Datum en tijd zijn niet geldig.'
                })

        if form.is_valid():
            form.save()
            return redirect('/account/dashboard')

        else:
            return render(request, 'account/edit_event.html', {
                'form': form,
                'error': 'Er is een fout opgetreden bij het bijwerken van het event.'
            })

    else:
        form = EventForm(instance=event)

    return render(request, 'account/edit_event.html', {
        'form': form,
        'films': Film.objects.all(),
        'locations': Location.objects.all(),
        'rooms': Room.objects.all(),
    })
