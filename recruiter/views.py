from django.shortcuts import render

# Create your views here.


def RecruiterLanding(request):
    template = "recruiter/RecruiterLanding.html"
    return render(request,template)

def RecruiterRegistration(request):
    template = "recruiter/RecruiterRegistration.html"
    return render(request, template)

def AvailableInterns(request):
    template = "recruiter/AvailableInterns.html"
    return render(request, template)

def add_Interns(request):
    template = "recruiter/AvailableInterns.html"
    return render(request, template)

def ShortlistedInterns(request):
    template = "recruiter/ShortlistedInterns.html"
    return render(request, template)

def CompanyProfile(request):
    template = "recruiter/CompanyProfile.html"
    return render(request, template)


def random_template(request):
    return render(request,"recruiter/base1.html")