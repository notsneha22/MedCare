from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            "doctor",
            "appointment_date",
            "appointment_time",
            "reason",
        ]

        widgets = {
            "doctor": forms.Select(attrs={
                "class": "w-full border rounded-lg p-2"
            }),

            "appointment_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "w-full border rounded-lg p-2"
                }
            ),

            "appointment_time": forms.TimeInput(
                attrs={
                    "type": "time",
                    "class": "w-full border rounded-lg p-2"
                }
            ),

            "reason": forms.Textarea(
                attrs={
                    "class": "w-full border rounded-lg p-2",
                    "rows": 4
                }
            ),
        }