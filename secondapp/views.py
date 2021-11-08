
from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    data = "Welcome to Second Application Home page"
    return HttpResponse(data)
