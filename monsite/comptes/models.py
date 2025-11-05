from django.contrib.auth.models import AbstractUser
from django.db import models


class Utilisateur(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('tuteur', 'Tuteur'),
        ('etudiant', 'Étudiant'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='etudiant')
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='profils/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
