from django.shortcuts import render
from .models import Medicine
# Create your views here.

def medicine_list(request):

    medicines = Medicine.objects.filter(
        available=True
    )

    return render(
        request,
        "pharmacy/medicine_list.html",
        {
            "medicines": medicines
        },
    )