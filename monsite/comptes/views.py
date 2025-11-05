from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm, ProfilForm, RegisterForm


# --- INSCRIPTION ---
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie !")
            # 🔸 Redirection selon rôle
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'tuteur':
                return redirect('tuteur_dashboard')
            else:
                return redirect('etudiant_dashboard')
    else:
        form = RegisterForm()
    return render(request, 'comptes/register.html', {'form': form})


# --- CONNEXION ---
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Connexion réussie !")
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'tuteur':
                return redirect('tuteur_dashboard')
            else:
                return redirect('etudiant_dashboard')
        messages.error(request, "Identifiants invalides. Veuillez réessayer.")
    else:
        form = LoginForm(request)
    return render(request, 'comptes/login.html', {'form': form})





# --- DÉCONNEXION ---
def logout_view(request):
    logout(request)
    messages.info(request, "Vous êtes déconnecté.")
    return redirect('login')


# --- DASHBOARDS PAR RÔLE ---
@login_required
def admin_dashboard(request):
    context = {
        'user': request.user,
        'role': 'Administrateur',
        'message': "Espace administrateur — gérez les utilisateurs du site 👑",
        'color': "#ff6b6b",
        'details': [
            {"name": "Gérer les comptes", "url": "#"},
            {"name": "Voir les statistiques", "url": "#"},
            {"name": "Superviser les tuteurs", "url": "#"}
        ]
    }
    return render(request, 'comptes/admin_dashboard.html', context)


@login_required
def tuteur_dashboard(request):
    context = {
        'user': request.user,
        'role': 'Tuteur',
        'message': "Espace tuteur — suivez vos étudiants 🎓",
        'color': "#4ecdc4",
        'details': [
            {"name": "Consulter la liste des étudiants", "url": "#"},
            {"name": "Donner un feedback", "url": "#"},
            {"name": "Voir les progrès", "url": "#"}
        ]
    }
    return render(request, 'comptes/tuteur_dashboard.html', context)


@login_required
def etudiant_dashboard(request):
    context = {
        'user': request.user,
        'role': 'Étudiant',
        'message': "Espace étudiant — bienvenue dans ton espace d’apprentissage 🌸",
        'color': "#6c63ff",
        'details': [
            {"name": "Modifier ton profil", "url": "profil"},
            {"name": "Voir tes notes", "url": "#"},
            {"name": "Accéder à ton emploi du temps", "url": "#"}
        ]
    }
    return render(request, 'comptes/etudiant_dashboard.html', context)


# --- PROFIL ---
@login_required
def profil_view(request):
    user = request.user
    if request.method == 'POST':
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        photo = request.FILES.get('photo')

        user.email = email
        user.bio = bio
        if photo:
            user.photo = photo
        user.save()
        messages.success(request, "Profil mis à jour.")
        return redirect('etudiant_dashboard')

    return render(request, 'comptes/profil.html', {'user': user})


# --- ÉDITION DU PROFIL ---
@login_required
def edit_profil_view(request):
    user = request.user
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre profil a bien été modifié.")
            return redirect('profil')
    else:
        form = ProfilForm(instance=user)
    return render(request, 'comptes/edit_profil.html', {'form': form})






