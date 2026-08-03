from django.db import models
from django.conf import settings


class Patient(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=10,
        choices=[
            ("Male", "Male"),
            ("Female", "Female"),
            ("Other", "Other"),
        ],
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    blood_group = models.CharField(
        max_length=5,
        choices=[
            ("A+", "A+"),
            ("A-", "A-"),
            ("B+", "B+"),
            ("B-", "B-"),
            ("AB+", "AB+"),
            ("AB-", "AB-"),
            ("O+", "O+"),
            ("O-", "O-"),
        ],
        blank=True
    )

    profile_picture = models.ImageField(
        upload_to="patients/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user.username