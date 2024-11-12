from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.homeView, name="homeView"),
    path("contact/", views.contactView, name="contactView"),
    path("mode/<mode>/", views.modeView, name="modeView"),
]