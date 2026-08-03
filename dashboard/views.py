from django.shortcuts import render
from doctors.models import Doctor
from appointments.models import Appointment
from billing.models import Billing
from lab_reports.models import LabReport


def dashboard(request):

    context = {
        "doctor_count": Doctor.objects.count(),

        "appointment_count": Appointment.objects.filter(
            patient=request.user
        ).count(),

        "bill_count": Billing.objects.filter(
            patient=request.user
        ).count(),

        "report_count": LabReport.objects.filter(
            appointment__patient=request.user
        ).count(),
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )