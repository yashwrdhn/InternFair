from django.shortcuts import render

from django.http import HttpResponse
from internfair.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
from internfair.models import *
from .models import *
def RecruiterLanding(request):

    # if (request.POST):
    #
    template = "recruiter/RecruiterLanding.html"
    # email =

    return render(request,template)







# def RecruiterRegistration(request):
#     template = "recruiter/RecruiterRegistration.html"
#     return render(request, template)


def AvailableInterns(request,**kwargs):

    template = "recruiter/AvailableInterns.html"
    current_user = request.user
    startup_object = StartUps.objects.get(user=current_user)
    return render(request, template,{'startup': startup_object})

def add_profiles(request):
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





def intern_form(request):

    if request.method == "POST":
        print(request.POST)
        startup = StartUps.objects.get(user=request.user)
        profile = request.POST["PROFILE"]
        stipend = request.POST["STIPEND"]
        allowances = request.POST["ALLOWANCE"]
        location = request.POST["LOCATION"]
        questions =  { request.POST["Q1"],request.POST["Q2"],request.POST["Q3"] }

        form = Intern_form.objects.create(startup = startup,stipend=stipend,allowances=allowances,location=location,questions=questions)
        form.save()
        print(form)
        return HttpResponse("done")

    else :

        template = "recruiter/AvailableInterns.html"
        return render(request, template)

