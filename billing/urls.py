from django.urls import path
from . import views

urlpatterns = [
    path("", views.billing_list, name="billing"),

    path(
        "pay/<int:id>/",
        views.pay_bill,
        name="pay_bill"
    ),
]