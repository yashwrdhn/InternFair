from django.shortcuts import render
from django.views import View
# Create your views here.

def index(request):
    return render(request, "StudentLanding.html")

def StudentRegistration(request):
    return render(request, "StudentRegistration.html")

def StudentProfile(request):
    return render(request, "StudentProfile1.html")

def AvailableInternships(request):
    return render(request, "AvailableInternships.html")







