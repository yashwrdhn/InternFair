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
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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

@login_required
def StudentProfile(request,**kwargs):

    user = Students.objects.get(user=request.user)
    registered_internships = InternApplication.objects.filter(Intern__id = user.pk)
    print(registered_internships)
    return render(request, "StudentProfile1.html",{'student':user,'interns':registered_internships})


def studentLogin(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active and user.is_student:
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
            if user.is_active and user.is_startup:
                login(request,user)
                return HttpResponseRedirect(reverse('recruiter:Profile',kwargs={'pk': user.id}))
                return redirect('../recruiter/profile')
            else:
                return redirect('../recruiter',{'error':'User is flagged Inactive. Drop mail to internfair@udgam.in to reactivate your account'})
        else:

            return redirect('../recruiter',{'error':'Invalid login details given'})
    else:
        return redirect('../recruiter')



@login_required
def AvailableInternships(request):
    if request.method == "POST":
        print(request.POST)
        student = Students.objects.get(user=request.user)
        startup = request.POST["startup"]
        profile = request.POST["profile"]
        id = request.POST['id']
        internship = Intern_form.objects.get(pk=id)
        answers  = request.POST.getlist("answers")
        CV  = request.POST["CV"]
        print(internship.location)
        app = InternApplication.objects.create(Intern=student,Internship = internship, Answers=answers,CV = CV)
        # app = [student.name,startup,profile,internship,answers]
        print(app)
        return redirect('StudentProfile')

    else:
        available_internships = Intern_form.objects.all()

        template = "AvailableInternships.html"
        context = {'interns': available_internships}

        return render(request, template, context)


@login_required
def EditStudProfile(request, **kwargs):
    current_user = request.user
    student = Students.objects.get(user=current_user)
    if request.method=='POST':
        if request.POST['roll_number']:
            student.roll_number = request.POST['roll_number']
        if request.POST['department']:
            student.department = request.POST['department']
        if request.POST['bio']:
            student.bio = request.POST['bio']
        student.save()
    return HttpResponseRedirect(reverse('StudentProfile',kwargs={'pk': current_user.id}))







@login_required
def logout_view(request):
    logout(request)
    return redirect( 'index')

@login_required
def delete_app(request,**kwargs):
    print(kwargs)
    id = kwargs['pk']
    student = Students.objects.get(user = request.user)
    print(student)
    intern_app = InternApplication.objects.get(pk = id)
    intern_app.delete()

    print(intern_app)


    return HttpResponseRedirect(reverse('StudentProfile',kwargs={'pk': student.id}))