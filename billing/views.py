from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Billing


@login_required
def billing_list(request):

    bills = Billing.objects.filter(
        patient=request.user
    )

    return render(
        request,
        "billing/billing.html",
        {
            "bills": bills
        }
    )


@login_required
def pay_bill(request, id):

    bill = get_object_or_404(
        Billing,
        id=id,
        patient=request.user
    )

    bill.payment_status = "Paid"
    bill.save()

    return redirect("billing")