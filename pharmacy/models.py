from django.db import models

# Create your models here.

class Medicine(models.Model):

    name = models.CharField(max_length=100)

    manufacturer = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(default=0)

    expiry_date = models.DateField()

    image = models.ImageField(
        upload_to="medicines/",
        blank=True,
        null=True,
    )

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name