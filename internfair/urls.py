from django.urls import path
from . import views
from django.shortcuts import  render
urlpatterns = [
    path('', views.index, name='index'),
    path('student/register', views.StudentRegistration, name='StudentRegistration'),
    path('student/profile', views.StudentProfile, name='StudentProfile'),
    path('student/availableInternships', views.AvailableInternships, name='AvailableInternships'),
    path('recruiter/',views.RecruiterLanding, name='RecruiterLanding'),
    path('recruiter/registration/',views.RecruiterRegistration, name='RecruiterRegistration'),
    path('recruiter/interns',views.AvailableInterns, name='InternList'),
    path('recruiter/profile',views.CompanyProfile, name='Profile'),
    path('recruiter/', lambda request: render(request, 'InternAnswerCard.html'))

]
