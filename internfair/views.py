from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.views import View
from internfair.forms  import *
from internfair.models import *
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from .models import User

# Create your views here.

def index(request):
    return render(request, "StudentLanding.html")

class StudentRegistration(CreateView):
    model = User
    form_class = StudentsForm
    template_name = './StudentRegistration.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('../profile')

class StartUpsRegistration(CreateView):
    model = User
    form_class = StartUpsForm
    template_name = 'recruiter/RecruiterRegistration.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'startup'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('../recruiter/profile')

def StudentProfile(request):
    return render(request, "StudentProfile1.html")

def AvailableInternships(request):
    return render(request, "AvailableInternships.html")


