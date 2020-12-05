from django.urls import include, path
from . import views
from internfair import views as stViews

app_name = 'recruiter'

urlpatterns = [

    path('', views.RecruiterLanding, name='RecruiterLanding'),
    path('registration', stViews.StartUpsRegistration.as_view(), name='RecruiterRegistration'),
    path(r'^interns/(?P<pk>\d+)/$', views.AvailableInterns, name='InternList'),
    path(r'^shortlist/(?P<pk>\d+)/$', views.ShortlistedInterns, name='shortlistedInterns'),
    path(r'^profile/(?P<pk>\d+)/$', views.CompanyProfile, name='Profile'),
    path(r'^profile/edit/(?P<pk>\d+)/$', views.EditStartupProfile, name='editStartupProfile'),
    path('preview', views.random_template, name='test_preview'),
    path('login',stViews.startupLogin, name='StartupLogin'),

]