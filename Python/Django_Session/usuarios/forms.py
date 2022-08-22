from django.contrib.auth import forms
from .models import Users

class UserChangeForm(forms.UserChangeForm):
    class Meta (forms.UserChangeForm.Meta):
        model = Users

class UserCreationForm(forms.UserChangeForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users