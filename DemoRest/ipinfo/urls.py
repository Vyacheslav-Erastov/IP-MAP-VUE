from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('ipinfo/ip/', views.IPInfoView.as_view()),
]