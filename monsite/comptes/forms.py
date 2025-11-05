from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Utilisateur


# --- FORMULAIRE D’INSCRIPTION ---
class RegisterForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'role', 'password1', 'password2']


# --- FORMULAIRE DE CONNEXION ---
class LoginForm(AuthenticationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'password']


# --- FORMULAIRE DE PROFIL ---
class ProfilForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['email', 'bio', 'photo']
