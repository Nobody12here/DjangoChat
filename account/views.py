from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Profile
from .forms import ProfileForm, CustomUserForm
from django.contrib.auth import authenticate,login as auth_login


def login(request: HttpRequest):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        message = "Logged in sucessfully"
        if user:
            auth_login(request,user)
            context = {"message": message}
            return redirect("create-room")
        if not user:
            message = "Invalid credentials"
    else:
        return render(request, "account/login.html")


def signup(request: HttpRequest):
    if request.method == "POST":
        user_form = CustomUserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            profile_picture = profile_form.cleaned_data.get("profile_picture")
            user = user_form.save()
            profile = Profile.objects.create(user=user, profile_picture=profile_picture)
            profile.save()
            return redirect("login")

    else:
        user_form = CustomUserForm()
        profile_form = ProfileForm()
    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, "account/signup.html", context)
