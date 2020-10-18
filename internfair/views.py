from django.shortcuts import render
from django.views import View
# Create your views here.

def index(request):
    return render(request, "StudentLanding.html")






def RecruiterLanding(request):
    template = "RecruiterLanding.html"
    return render(request,template)

def RecruiterRegistration(request):
    template = "RecruiterRegistration.html"
    context = []
    return render(request, template,context)

def AvailableInterns(request):
    template = "AvailableInterns.html"
    context = []
    return render(request, template,context)

def CompanyProfile(request):
    template = "CompanyProfile.html"
    context  = []
    return render(request, template,context)