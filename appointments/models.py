from django.db import models
from django.conf import settings
from doctors.models import Doctor


class Appointment(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    TIME_SLOTS = [
        ("09:00", "09:00 AM"),
        ("09:30", "09:30 AM"),
        ("10:00", "10:00 AM"),
        ("10:30", "10:30 AM"),
        ("11:00", "11:00 AM"),
        ("11:30", "11:30 AM"),
        ("12:00", "12:00 PM"),
        ("14:00", "02:00 PM"),
        ("14:30", "02:30 PM"),
        ("15:00", "03:00 PM"),
        ("15:30", "03:30 PM"),
        ("16:00", "04:00 PM"),
    ]

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    appointment_date = models.DateField()

    appointment_time = models.CharField(
        max_length=5,
        choices=TIME_SLOTS,
    )

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending",
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.patient.username} - Dr. {self.doctor.first_name}"