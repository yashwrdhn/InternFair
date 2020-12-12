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
    status = { ('ACTIVE','ACTIVE'),('DEACTIVE','DEACTIVE')}
    FormStatus = models.CharField(max_length=10,choices=status,default='ACTIVE')
    remarks = models.CharField(max_length=200,default=".")
    def string_as_list(self):
        print(self.questions)
        ques = self.questions.split(',')
        print(ques)
        for q in ques:
            if q == '':
                ques.remove(q)
        print(ques)
        return ques


    def __str__(self):
        return str(self.startup.user) + '-' +self.profile

    def Applicant_count(self):
        available = InternApplication.objects.filter(Internship__startup=self.startup).filter(Internship__profile=self.profile).filter(
            Status="PENDING").count()
        return available
    def Shortlisted_count(self):
        shortlisted = InternApplication.objects.filter(Internship__startup=self.startup).filter(Internship__profile=self.profile).filter(
            Status="SHORTLISTED").count()
        return shortlisted


class InternApplication(models.Model):
    status = { ('PENDING','pending'),('SHORTLISTED','shortlisted'),('REJECTED','rejected')}
    Intern = models.ForeignKey(Students,on_delete=models.CASCADE)
    Internship = models.ForeignKey(Intern_form,on_delete = models.CASCADE)
    Status = models.CharField(max_length=20,choices=status,default='PENDING')
    Answers = models.TextField(max_length=400)
    CV  = models.CharField(max_length=500,default="not submitted")
    def __str__(self):
        return '{}-{}'.format(self.Intern,self.Internship)

    def count_intern_Answers(self):
        ans = self.Answers.strip('[]')
        ans_list = ans.split(',')
        # print(ans_list)
        len(ans_list)
        # print(len)
        # print(self.questions)
        ques = self.Internship.questions
        # print(ques)
        ques_list = ques.split(',')
        # print(ques)
        print(ques)
        for q in ques_list:
            if q == '':
                ques_list.remove(q)
        print(ques_list)

        QnA = dict(zip(ques_list,ans_list))
        return QnA

    def if_shortlisted(self):
        if self.Status == 'SHORTLISTED':
            print(self.Status, 'congrats')
            return True
        else:
            return False
