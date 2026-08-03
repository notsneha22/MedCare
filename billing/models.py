from django.db import models
from appointments.models import Appointment
from django.conf import settings
# Create your models here.

class Billing(models.Model):

    PAYMENT_STATUS = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
    ]

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE
    )

    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    medicine_charge = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    lab_charge = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="Pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.patient.username} - ₹{self.amount}"