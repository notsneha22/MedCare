from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import redirect
from .forms import RegisterForm
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
def home(request):
    return render(request, "home.html")


def user_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
             if user is not None:
              login(request, user)
              return redirect("dashboard")

    return render(request, "accounts/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")

def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})

def change_password(request):

    if request.method == "POST":

        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(request, user)
            return redirect("dashboard")

    else:

        form = PasswordChangeForm(request.user)

    return render(
        request,
        "accounts/change_password.html",
        {
            "form": form
        }
    )