from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# ✅ Définition de la fonction accueil
def accueil(request):
    return HttpResponse("""
        <html lang='fr'>
        <head>
            <meta charset='UTF-8'>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <title>Accueil</title>
        </head>
        <body style="font-family: Poppins, sans-serif; background: #f7f7ff; text-align:center; margin-top: 80px;">
            <h1>Bienvenue sur mon projet Django 🌸</h1>
            <p>Choisis une action :</p>
            <a href='/comptes/register/' style="background:#b57edc;color:white;padding:10px 20px;border-radius:8px;text-decoration:none;margin-right:10px;">Créer un compte</a>
            <a href='/comptes/login/' style="background:#6c63ff;color:white;padding:10px 20px;border-radius:8px;text-decoration:none;">Se connecter</a>
        </body>
        </html>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comptes/', include('comptes.urls')),
    path('', accueil),  # ✅ page d'accueil ajoutée
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
