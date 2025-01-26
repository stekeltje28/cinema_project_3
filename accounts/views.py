from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import json
from .models import CustomUser, UserData
from films.models import Film, Location, Room
from reserveringen.models import Event, Reservering
from django.contrib.auth.decorators import login_required
from .models import UserData
from django.shortcuts import get_object_or_404

from django.http import JsonResponse
from django.contrib.auth import login
from .models import CustomUser, UserData

def register(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password1 = data.get('password1')
            password2 = data.get('password2')
            name = data.get('name')
            leeftijd = data.get('leeftijd')

            if password1 != password2:
                return JsonResponse({'error': 'Wachtwoorden komen niet overeen'}, status=400)

            if CustomUser.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Er bestaat al een gebruiker met dit e-mailadres.'}, status=400)

            user = CustomUser.objects.create_user(email=email, password=password1, name=name, leeftijd=leeftijd)

            user_data = UserData.objects.create(
                user=user,
                naam=name,
                leeftijd=leeftijd,
            )

            login(request, user)

            return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'POST vereist'}, status=405)


def user_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('email')
            password = data.get('password')

            if not username or not password:
                return JsonResponse({'message': 'Email en wachtwoord zijn verplicht.'}, status=400)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Inloggen succesvol!', 'is_logged_in': True})
            else:
                return JsonResponse({'message': 'Ongeldige inloggegevens.', 'is_logged_in': False})

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Ongeldig JSON-formaat.', 'is_logged_in': False})

    return JsonResponse({'message': 'Alleen POST-verzoeken worden ondersteund.', 'is_logged_in': False})


def user_logout(request):
    logout(request)
    return JsonResponse({'success': True})


def check_logged_in(request):
    return JsonResponse({'is_logged_in': request.user.is_authenticated})


@login_required
def dashboard(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Je moet ingelogd zijn om toegang te krijgen tot het dashboard.'}, status=401)

    user_data, created = UserData.objects.get_or_create(user=request.user)

    if request.user.is_superuser:
        locations = Location.objects.all()
        rooms = Room.objects.all()
        films = Film.objects.all()
        events = Event.objects.all()

        return render(request, 'pages/user_pages/medewerkers_dashboard.html', {
            'locations': locations,
            'rooms': rooms,
            'films': films,
            'events': events,
            'user_data': user_data,
        })
    else:

        reserveringen = Reservering.objects.filter(gebruiker=request.user).select_related('event__film')
        opgeslagen_films = user_data.opgeslagen.all()  

        aantal_recente_reserveringen = reserveringen.count()

        return render(request, 'pages/user_pages/user_dashboard.html', {
            'user_data': user_data,
            'reserveringen': reserveringen,
            'aantal_recente_reserveringen': aantal_recente_reserveringen,
            'opgeslagen_films': opgeslagen_films,
        })

@login_required
def remove_film_from_smaakprofiel(request, film_id):
    user_data = UserData.objects.get(user=request.user)
    film = Film.objects.get(id=film_id)

    if film in user_data.opgeslagen_films.all():
        user_data.opgeslagen_films.remove(film)
        return render('/accounts/dashboard')
    else:
        return render('/accounts/dashboard')


@login_required
def save_film(request, film_id):
    try:

        film = get_object_or_404(Film, id=film_id)

        user_data, created = UserData.objects.get_or_create(user=request.user)

        user_data.opgeslagen.add(film)

        return redirect('film_detail', film_id=film.id)

    except Exception as e:

        return JsonResponse({'error': str(e)}, status=400)

@login_required
def toggle_film_save(request, film_id):
    try:
        film = get_object_or_404(Film, id=film_id)
        user_data, created = UserData.objects.get_or_create(user=request.user)

        if film in user_data.opgeslagen.all():
            user_data.opgeslagen.remove(film)
            action = "removed"
        else:
            user_data.opgeslagen.add(film)
            action = "saved"

        return redirect('film_detail', film_id=film.id)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)



