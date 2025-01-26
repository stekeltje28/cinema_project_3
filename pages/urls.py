from django.contrib import admin
from django.urls import path, include
from pages import views

urlpatterns = [
    path('', views.index , name='index'),
    path('account/', include('accounts.urls')),
    path('', include('films.urls'))
]