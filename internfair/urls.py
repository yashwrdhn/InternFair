from django.urls import path
from . import views
from django.shortcuts import  render
urlpatterns = [
    path('student/', views.index, name='index'),




    path('recruiter/',views.RecruiterLanding, name='RecruiterLanding'),
    path('recruiter/registration/',views.RecruiterRegistration, name='RecruiterRegistration'),
    path('recruiter/interns',views.AvailableInterns, name='InternList'),
    path('recruiter/profile',views.CompanyProfile, name='Profile'),
    path('recruiter/', lambda request: render(request, 'InternAnswerCard.html'))

]
