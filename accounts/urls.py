from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from reserveringen import views as reservering_views
from accounts import views as accounts_views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('check-logged-in/', views.check_logged_in, name='check_logged_in'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('remove_film/<int:film_id>/', accounts_views.remove_film_from_smaakprofiel,name='remove_film_from_smaakprofiel'),

    path('assign/', reservering_views.assign_film_date_location, name='assign_film_date_location'),
    path('edit_event/<int:event_id>/', reservering_views.edit_event, name='edit_event'),
    path('update_event/<int:event_id>', reservering_views.update_event, name='update_event'),
    path('update-reservering/<int:reservering_id>/',reservering_views.update_reservering, name='update_reservering'),
    path('reservering/delete/<int:reservering_id>/', reservering_views.delete_reservation, name='delete_reservation'),
    path('toggle_film_save/<int:film_id>/', views.toggle_film_save, name='toggle_film_save'),

]
