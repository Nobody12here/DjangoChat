from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate

def login(request:HttpRequest):
    if request.method == "POST":
        email = request.POST.get("email")
        password =  request.POST.get("password")
        user = authenticate(email="test@gmail.com",password="test123")
        print(email,password)
        print(user)
        return render(request, "account/login.html")
    else:
        return render(request, "account/login.html")
