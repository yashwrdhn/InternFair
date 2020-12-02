from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.views import View
from internfair.forms  import *
from internfair.models import *
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

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
        return HttpResponseRedirect(reverse('StudentProfile',kwargs={'pk': user.id}))


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
        return HttpResponseRedirect(reverse('recruiter:Profile',kwargs={'pk': user.id}))

def StudentProfile(request,**kwargs):
    current_user = request.user
    stud_object = Students.objects.get(user=current_user)
    return render(request, "StudentProfile1.html", {'student' : stud_object})

def AvailableInternships(request):
    return render(request, "AvailableInternships.html")


def studentLogin(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('StudentProfile',kwargs={'pk': user.id}))
                # return redirect('/student/profile',kwargs={'pk': user.id})
            else:
                return redirect('/',{'error':'User is flagged Inactive. Drop mail to internfair@udgam.in to reactivate your account'})
        else:
            return redirect('/', {'error':'Invalid login details given'})
    else:
        return redirect('/')

def startupLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('recruiter:Profile',kwargs={'pk': user.id}))
                return redirect('../recruiter/profile')
            else:
                return redirect('../recruiter',{'error':'User is flagged Inactive. Drop mail to internfair@udgam.in to reactivate your account'})
        else:

            return redirect('../recruiter',{'error':'Invalid login details given'})
    else:
        return redirect('../recruiter')

