
from django.urls import path
from . import views
from reserveringen.views import reservering

urlpatterns = [
    path('locations/', views.location_list, name='location_list'),
    path('locations/add/', views.add_location, name='add_location'),
    path('location/<int:location_id>/delete/', views.delete_location, name='delete_location'),
    path('locations//add-room/', views.add_room, name='add_room'),
    path('room/<int:room_id>/delete/', views.delete_room, name='delete_room'),

    path('films/', views.film_list, name='films'),
    path('films/add/', views.add_film, name='add_film'),
    path('films/<int:film_id>/', views.film_detail, name='film_detail'),
    path('films/list/', views.film_list, name='film_list'),
    path('films/reservering/<int:film_id>/', reservering, name='reservering'),

]
