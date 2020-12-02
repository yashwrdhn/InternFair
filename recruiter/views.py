from django.shortcuts import render
from internfair.models import *

# Create your views here.


def RecruiterLanding(request):
    template = "recruiter/RecruiterLanding.html"
    return render(request,template)

# def RecruiterRegistration(request):
#     template = "recruiter/RecruiterRegistration.html"
#     return render(request, template)

def AvailableInterns(request,**kwargs):
    template = "recruiter/AvailableInterns.html"
    current_user = request.user
    startup_object = StartUps.objects.get(user=current_user)
    return render(request, template,{'startup': startup_object})

def add_Interns(request):
    template = "recruiter/AvailableInterns.html"
    return render(request, template)

def ShortlistedInterns(request,**kwargs):
    template = "recruiter/ShortlistedInterns.html"
    current_user = request.user
    startup_object = StartUps.objects.get(user=current_user)
    return render(request, template,{'startup': startup_object})

def CompanyProfile(request,**kwargs):
    current_user = request.user
    startup_object = StartUps.objects.get(user=current_user)
    template = "recruiter/CompanyProfile.html"
    return render(request, template,{'startup': startup_object})


def random_template(request):
    return render(request,"recruiter/CompanyDetailsCard.html")