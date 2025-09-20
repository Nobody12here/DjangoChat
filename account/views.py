from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth import authenticate


def login(request: HttpRequest):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        message = "Logged in sucessfully"
        if not user:
            message = "Invalid credentials"
        context = {"message": message}
        return render(request, "account/login.html", context)
    else:
        return render(request, "account/login.html")
