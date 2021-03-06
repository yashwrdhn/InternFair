from django.urls import include, path
from . import views
from django.shortcuts import  render
urlpatterns = [
    path('', views.index, name='index'),

    path('student/register', views.StudentRegistration.as_view(), name='StudentRegistration'),
    path('student/profile', views.StudentProfile, name='StudentProfile'),

    # path('student/register/', views.StudentRegistration.as_view(), name='StudentRegistration'),
    path(r'^student/profile/(?P<pk>\d+)/$', views.StudentProfile, name='StudentProfile'),
    path(r'^student/profile/edit/(?P<pk>\d+)/$', views.EditStudProfile, name='editStudentProfile'),
    path('student/profile/delete/<int:pk>',views.delete_app,name='delete_app'),
    path('student/availableInternships', views.AvailableInternships, name='AvailableInternships'),
    path('student/login', views.studentLogin, name='StudentLogin'),
    path('student/logout', views.logout_view, name='StudentLogout'),
]
