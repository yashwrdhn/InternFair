from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.views import View
from .forms  import *
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from recruiter.models import *
from django.contrib import messages

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
        return redirect('./profile')

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

    user = Students.objects.get(user=request.user)
    print(user.department)
    if user:
        return render(request, "StudentProfile1.html",{'user':user})
    else:
        return HttpResponse("u r not logged in ")


def studentLogin(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/student/profile')
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
                return redirect('../recruiter/profile')
            else:
                return redirect('../recruiter',{'error':'User is flagged Inactive. Drop mail to internfair@udgam.in to reactivate your account'})
        else:

            return redirect('../recruiter',{'error':'Invalid login details given'})
    else:
        return redirect('../recruiter')



def AvailableInternships(request):
    if request.method == "POST":
        print(request.POST)
        student = Students.objects.get(user=request.user)
        startup = request.POST["startup"]
        profile = request.POST["profile"]
        internship = Intern_form.objects.filter(startup__companyName=startup ).get(profile=profile)
        answers  = request.POST.getlist("answers")
        print(internship.location)
        app = InternApplication.objects.create(Intern=student,Internship = internship, Answers=answers)
        # app = [student.name,startup,profile,internship,answers]
        print(app)
        return redirect('./profile')

    else:
        available_internships = Intern_form.objects.all()

        template = "AvailableInternships.html"
        context = {'interns': available_internships}

        return render(request, template, context)
