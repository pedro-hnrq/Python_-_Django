from django.contrib import admin
from .models import Users
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth import admin as admin_auth_django

@admin.register(Users)
class UserAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "rua")
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Informações recidenciais', {'fields':('rua','cep', 'numero')}),
    )
    #Não Aterar no ADMIM 
    readonly_fields = ('rua','numero', 'cep')
    # fieldsets = (("Informações Residenciais", {'fiels':('rua','cep', 'numero')}),)
# admin.site.register(Users)