from django import forms
from internfair.models import *
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.db import transaction

class StartUpsForm(UserCreationForm):
    email = forms.EmailField(max_length=150)
    POC = forms.CharField(max_length=50)
    contact = forms.IntegerField(label='Contact No.')
    companyName = forms.CharField(max_length=100)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','POC','contact','companyName','password1', 'password2',)   

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_startup = True
        user.save()
        startup = StartUps.objects.create(user=user)
        startup.email=self.cleaned_data.get('email')
        startup.POC=self.cleaned_data.get('POC')
        startup.companyName=self.cleaned_data.get('companyName')
        startup.contact=self.cleaned_data.get('contact')
        startup.save()
        return user

class StudentsForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    roll_number = forms.CharField(max_length=13)
    email = forms.EmailField(max_length=150)
    department = forms.CharField(max_length=50)
    contact= forms.CharField(max_length=10, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('name','username','email','roll_number','department','contact','password1', 'password2',)
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student =Students.objects.create(user=user)
        student.name=self.cleaned_data.get('name')
        student.roll_number=self.cleaned_data.get('roll_number')
        student.email=self.cleaned_data.get('email')
        student.department=self.cleaned_data.get('department')
        student.contact=self.cleaned_data.get('contact')
        student.save()
        return user

class ApplicationForm(forms.Form):
    resume = forms.FileField()
    content = forms.CharField(max_length=100)

class LogoForm(forms.Form):
    logo = forms.ImageField()