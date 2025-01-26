from django.contrib import admin
from .models import CustomUser, UserData
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):

    list_display = ('email', 'name', 'is_staff', 'is_superuser', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('email',)
    search_fields = ('email', 'name')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Persoonlijke informatie', {'fields': ('name',)}),
        ('Permissies', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        ('Belangrijke data', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

class UserDataAdmin(admin.ModelAdmin):

    list_display = ('user', 'naam', 'leeftijd', 'aantal_recente_reserveringen', 'profiel_foto')
    search_fields = ('naam', 'user__email')
    ordering = ('user__email',)

    fieldsets = (
        (None, {'fields': ('user', 'naam', 'leeftijd', 'profiel_foto')}),
        ('Reserveringen', {'fields': ('reserveringen', 'aantal_recente_reserveringen')}),
        ('Voorkeuren', {'fields': ('opgeslagen', 'favoriete_genres')}),
    )

admin.site.register(UserData, UserDataAdmin)
