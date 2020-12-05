from django.shortcuts import render
from internfair.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

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

def EditStartupProfile(request, **kwargs):
    current_user = request.user
    startup = StartUps.objects.get(user=current_user)
    if request.method=='POST':
        if request.POST['companyName']:
            startup.companyName = request.POST['companyName']
        if request.POST['description']:
            startup.description = request.POST['description']
        if request.POST['location']:
            startup.location = request.POST['location']
        startup.save()
    return HttpResponseRedirect(reverse('recruiter:Profile',kwargs={'pk': current_user.id}))

def random_template(request):
    return render(request,"recruiter/CompanyDetailsCard.html")

