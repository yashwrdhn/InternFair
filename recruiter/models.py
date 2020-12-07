from django.db import models
from internfair.models import *
# Create your models here.
class Intern_form(models.Model):
    startup = models.ForeignKey(StartUps, on_delete=models.CASCADE, related_name='intern_details')
    profile = models.CharField(max_length=50,blank=True)
    stipend = models.IntegerField(blank=True)
    location = models.CharField(max_length=50,blank=True)
    allowances = models.CharField(max_length=150,blank=True)
    questions = models.TextField(max_length=200)

    def string_as_list(self):
        # print(self.questions)
        ques = self.questions.strip('{}')
        # print(ques)
        ques =  ques.split(',')
        # print(ques)
        return ques


    def __str__(self):
        return self.profile




class InternApplication(models.Model):
    status = { (1,'PENDING'),(2,'SHORTLISTED'),(0,'REJECTED')}
    Intern = models.ForeignKey(Students,on_delete=models.CASCADE)
    Internship = models.ForeignKey(Intern_form,on_delete = models.CASCADE)
    Status = models.CharField(max_length=20,choices=status,default=1)
    Answers = models.TextField(max_length=200)

    def __str__(self):
        return '{}-{}'.format(self.Intern,self.Internship)