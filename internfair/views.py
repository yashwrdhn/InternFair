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



def RecruiterLanding(request):
    template = "RecruiterLanding.html"
    return render(request,template)

def RecruiterRegistration(request):
    template = "RecruiterRegistration.html"
    return render(request, template)

def AvailableInterns(request):
    template = "AvailableInterns.html"
    return render(request, template)

def CompanyProfile(request):
    template = "CompanyProfile.html"
    return render(request, template)


def random_template(request):
    return render(request,"InternProfileCard.html")