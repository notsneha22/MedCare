from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ("ADMIN", "Admin"),
        ("DOCTOR", "Doctor"),
        ("PATIENT", "Patient"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="PATIENT",
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username
