from django.urls import path
from . import views

urlpatterns = [
    path(
        "book/",
        views.book_appointment,
        name="book_appointment"
    ),

    path(
        "my/",
        views.my_appointments,
        name="appointment"
        ),
     path(
        "cancel/<int:id>/",
        views.cancel_appointment,
        name="cancel_appointment",
    ),
]