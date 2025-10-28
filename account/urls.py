from django.urls import path
from account import views
from django.contrib.auth import views as AuthViews

urlpatterns = [
    path("logout/", views.logout, name="logout"),
    path("", views.login, name="login"),
    path("signup", views.signup, name="signup"),
]
