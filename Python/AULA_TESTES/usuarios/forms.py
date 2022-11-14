from django.forms import ModelForm
from .models import Usuario

class FormUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome','email','senha']