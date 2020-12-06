from django.urls import include, path
from . import views
from internfair import views as stViews

app_name = 'recruiter'

urlpatterns = [

    path('', views.RecruiterLanding, name='RecruiterLanding'),
    path('registration', stViews.StartUpsRegistration.as_view(), name='RecruiterRegistration'),
    path('interns', views.intern_form, name='InternList'),
    path('shortlist', views.ShortlistedInterns, name='shortlistedInterns'),
    path('profile', views.CompanyProfile, name='Profile'),
    path('preview', views.random_template, name='test_preview'),
    path('login',stViews.startupLogin, name='StartupLogin'),

]