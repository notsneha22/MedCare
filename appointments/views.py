from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import AppointmentForm
from .models import Appointment


@login_required
def book_appointment(request):

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():

            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()

            return redirect("appointment")

    else:

        form = AppointmentForm()

    return render(
        request,
        "appointments/book.html",
        {
            "form": form
        }
    )


@login_required
def my_appointments(request):

    appointments = Appointment.objects.filter(
        patient=request.user
    )

    status = request.GET.get("status")

    if status:
        appointments = appointments.filter(status=status)

    return render(
        request,
        "appointments/appointment.html",
        {
            "appointments": appointments,
            "selected_status": status,
        }
    )


@login_required
def cancel_appointment(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id,
        patient=request.user
    )

    if request.method == "POST":

        if appointment.status == "Pending":
            appointment.status = "Cancelled"
            appointment.save()

        return redirect("appointment")

    return render(
        request,
        "appointments/cancel_appointment.html",
        {
            "appointment": appointment
        }
    )