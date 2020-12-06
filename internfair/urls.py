from django.urls import path
from . import views
from django.shortcuts import  render
urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('student/register', views.StudentRegistration.as_view(), name='StudentRegistration'),
    path('student/profile', views.StudentProfile, name='StudentProfile'),
=======
    path('student/register/', views.StudentRegistration.as_view(), name='StudentRegistration'),
    path(r'^student/profile/(?P<pk>\d+)/$', views.StudentProfile, name='StudentProfile'),
    path(r'^student/profile/edit/(?P<pk>\d+)/$', views.EditStudProfile, name='editStudentProfile'),
>>>>>>> d49772b1175349da8fe6dd1a48fe58720e202c20
    path('student/availableInternships', views.AvailableInternships, name='AvailableInternships'),
    path('student/login', views.studentLogin, name='StudentLogin'),
]