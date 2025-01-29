from django.urls import path
from . import views
from reserveringen import views as reservation_views

urlpatterns = [
    #locaties
    path('locations/add/', views.add_location, name='add_location'),
    path('location/<int:location_id>/delete/', views.delete_location, name='delete_location'),
    path('locations/add-room/', views.add_room, name='add_room'),
    path('room/<int:room_id>/delete/', views.delete_room, name='delete_room'),
    #films
    path('films/', views.film_list, name='films'),
    path('films/add/', views.add_film, name='add_film'),
    path('films/remove', views.remove_film, name='remove_film'),
    path('films/<int:film_id>/', views.film_detail, name='film_detail'),
    path('films/list/', views.film_list, name='film_list'),
    path('films/reservering/<int:film_id>/', reservation_views.reservering, name='reservering'),
    path('films/delete_reservation/<int:film_id>/', reservation_views.delete_reservation, name='delete_reservation'),
    path('reservering-data/', reservation_views.reservering_data, name='reservering_data'),

]
