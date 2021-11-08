
from django.urls import path
from secondapp import views

urlpatterns = [
    path("home/", views.home_view),
]