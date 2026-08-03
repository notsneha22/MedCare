from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Patient
from .forms import PatientForm


@login_required
def profile(request):

    patient, created = Patient.objects.get_or_create(
        user=request.user
    )

    return render(
        request,
        "patients/profile.html",
        {
            "patient": patient
        }
    )


@login_required
def edit_profile(request):

    patient, created = Patient.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = PatientForm(
            request.POST,
            request.FILES,
            instance=patient
        )

        if form.is_valid():
            form.save()
            return redirect("patient_profile")

    else:

        form = PatientForm(
            instance=patient
        )

    return render(
        request,
        "patients/edit_profile.html",
        {
            "form": form
        }
    )