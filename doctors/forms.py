from django import forms
from .models import Doctor


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = [
            "first_name",
            "last_name",
            "specialization",
            "qualification",
            "experience",
            "consultation_fee",
            "phone",
            "email",
            "profile_picture",
            "available",
            "available_days",
            "start_time",
            "end_time",
        ]