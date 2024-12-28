from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser, ConfigurationCite

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bloc'].choices = ConfigurationCite.get_blocs_choices()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bloc'].choices = ConfigurationCite.get_blocs_choices()

@admin.register(ConfigurationCite)
class ConfigurationCiteAdmin(admin.ModelAdmin):
    list_display = ('nombre_blocs', 'date_modification')
    
    def has_add_permission(self, request):
        # Permettre l'ajout seulement s'il n'y a pas de configuration
        return not ConfigurationCite.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    
    list_display = ('username', 'email', 'role', 'bloc', 'est_actif')
    list_filter = ('role', 'est_actif', 'bloc')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name', 'email')}),
        ('Informations résidentielles', {'fields': ('role', 'telephone', 'address', 'bloc', 'nombre_voitures')}),
        ('Statut', {'fields': ('est_actif', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role', 'email', 'bloc'),
        }),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email', 'bloc')
    ordering = ('username',) 