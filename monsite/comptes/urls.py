from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboards selon le rôle
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('tuteur_dashboard/', views.tuteur_dashboard, name='tuteur_dashboard'),
    path('etudiant_dashboard/', views.etudiant_dashboard, name='etudiant_dashboard'),

    path('profil/', views.profil_view, name='profil'),
    path('edit_profil/', views.edit_profil_view, name='edit_profil'),
]

# Mots de passe
urlpatterns += [
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='comptes/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='comptes/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='comptes/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='comptes/password_reset_complete.html'), name='password_reset_complete'),
]
