from django.shortcuts import render
from django.http import HttpResponse
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


def AvailableInterns(request):
    template = "recruiter/AvailableInterns.html"
    return render(request, template)

def add_profiles(request):
    template = "recruiter/AvailableInterns.html"
    return render(request, template)

def ShortlistedInterns(request):
    template = "recruiter/ShortlistedInterns.html"
    return render(request, template)

def CompanyProfile(request):
    
    profiles =  Intern_form.objects.all()
    # for p in profiles:
    #     print(p)
    template = "recruiter/CompanyProfile.html"
    return render(request, template, {'profiles' :profiles} )


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