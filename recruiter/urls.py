from django.urls import include, path
from . import views

app_name = 'recruiter'
urlpatterns = [

    path('', views.RecruiterLanding, name='RecruiterLanding'),
    path('registration', views.RecruiterRegistration, name='RecruiterRegistration'),
    path('interns', views.AvailableInterns, name='InternList'),
    path('shortlist', views.ShortlistedInterns, name='shortlistedInterns'),
    path('profile', views.CompanyProfile, name='Profile'),
    path('preview', views.random_template, name='test_preview'),

]