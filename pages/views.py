from django.shortcuts import render
from accounts.models import UserData
from django.shortcuts import redirect

from django.shortcuts import render
from films.models import Film


def index(request):
    films = list(Film.objects.all())

    if len(films) <= 9:
        film_groups = [films] * 3
    elif len(films) <=3:
        film_groups = [films[i::3] for i in range(3)]
    else:
        return render(request, 'pages/index.html')

    return render(request, 'pages/index.html', {'film_groups': film_groups})
