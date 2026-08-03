from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.profile, name="patient_profile"),
    path("edit/", views.edit_profile, name="edit_profile"),
]