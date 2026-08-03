from django.db import models
from appointments.models import Appointment
# Create your models here.
class LabReport(models.Model):

    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE
    )

    report_name = models.CharField(max_length=100)

    report_file = models.FileField(
        upload_to="lab_reports/"
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.report_name
