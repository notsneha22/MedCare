from django.db import models


class Doctor(models.Model):

    SPECIALIZATION_CHOICES = [
        ("Cardiology", "Cardiology"),
        ("Dermatology", "Dermatology"),
        ("Neurology", "Neurology"),
        ("Orthopedics", "Orthopedics"),
        ("Pediatrics", "Pediatrics"),
        ("General Physician", "General Physician"),
    ]

    DAY_CHOICES = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    specialization = models.CharField(
        max_length=50,
        choices=SPECIALIZATION_CHOICES,
    )

    qualification = models.CharField(max_length=100)

    experience = models.PositiveIntegerField(
        help_text="Experience in years"
    )

    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    phone = models.CharField(max_length=15)

    email = models.EmailField(unique=True)

    profile_picture = models.ImageField(
        upload_to="doctors/",
        blank=True,
        null=True,
    )

    available = models.BooleanField(default=True)

    available_days = models.CharField(
        max_length=100,
        help_text="Example: Monday-Friday or Monday,Wednesday,Friday"
    )

    available_days = models.CharField(
    max_length=100,
    blank=True,
    default=""
)

start_time = models.TimeField(
    null=True,
    blank=True
)

end_time = models.TimeField(
    null=True,
    blank=True
)

created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"