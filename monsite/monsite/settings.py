"""Django settings for monsite project."""

from pathlib import Path
import os

# === BASE DIRECTORY ===
BASE_DIR = Path(__file__).resolve().parent.parent


# === CONFIGURATION DE BASE ===
SECRET_KEY = 'django-insecure-tsfczodb%vw%18qwk(1lb2n6!9(r^z$l^h=-e@1t7h1i*v^72y'
DEBUG = True
ALLOWED_HOSTS = []


# === APPLICATIONS INSTALLÉES ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # --- APP DU PROJET ---
    'comptes',
]


# === MIDDLEWARE ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# === ROUTES PRINCIPALES ===
ROOT_URLCONF = 'monsite.urls'


# === CONFIGURATION DES TEMPLATES ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Dossier global pour les templates si besoin
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# === APPLICATION WSGI ===
WSGI_APPLICATION = 'monsite.wsgi.application'


# === BASE DE DONNÉES ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# === VALIDATION DES MOTS DE PASSE ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# === PARAMÈTRES INTERNATIONAUX ===
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True


# === FICHIERS STATIQUES (CSS / JS) ===
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# === FICHIERS MÉDIAS (UPLOADS / PHOTOS PROFIL) ===
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# === CONFIGURATION DU MODÈLE UTILISATEUR PERSONNALISÉ ===
AUTH_USER_MODEL = 'comptes.Utilisateur'


# === CLÉ PRIMAIRE PAR DÉFAUT ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
