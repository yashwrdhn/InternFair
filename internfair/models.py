from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
import os


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.student.user.id, filename)

def user_directory_path1(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.id, filename)

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_startup = models.BooleanField(default=False)

class StartUps(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    POC = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    companyName = models.CharField(max_length=100, default="")
    contact = models.CharField(default="",max_length=10)
    logo = models.ImageField(upload_to=user_directory_path1,blank=True)
    description = models.CharField(max_length=500, default="Edit Profile to add description")
    location = models.CharField(max_length=100, default="Edit profile to add location")

    def __str__(self):
        return self.user.username

class Students(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='student')
    name = models.CharField(max_length=50,default="")
    roll_number = models.CharField(default="",max_length=13)
    department = models.CharField(max_length=50,default="")
    email = models.EmailField(max_length=150,default="")
    contact = models.CharField(default="",max_length=10)
    bio = models.CharField(default="Edit Profile to add bio",max_length=500)
    profilePhoto = models.ImageField(upload_to=user_directory_path,blank=True)
    
    def __str__(self):
        return self.user.username



# class  Application(models.Model):
#     STATUSES = (
#                 ('PENDING',"Pending") ,
#                 ('SHORTLISTED', "Shortlisted"),
#                 ('REJECTED', "Rejected")
#                 )
#     student = models.ForeignKey(Students ,on_delete=models.CASCADE, related_name='application')
#     intern_pos = models.ForeignKey(InternDetails,on_delete=models.CASCADE, related_name='proposal')
#     resume = models.FileField(upload_to=user_directory_path)
#     content = models.TextField(max_length=100)
#     status = models.CharField(max_length=20, null=True, choices=STATUSES, default='PENDING')

#     def __str__(self):
#         return str(self.student)+'-'+str(self.intern_pos)

# # To delete the resume after each application is deleted.
# @receiver(post_delete, sender=Application)
# def auto_delete_file_on_delete(sender, instance, **kwargs):
#     """
#     Deletes file from filesystem
#     when corresponding `MediaFile` object is deleted.
#     """
#     if instance.resume:
#         if os.path.isfile(instance.resume.path):
#             os.remove(instance.resume.path)

# class MaxValue(models.Model):
#     limit = models.IntegerField()

#     def __str__(self):
#         return str(self.limit)
# # @receiver(post_save, sender=User)
# # def update_registration_signal(sender, instance, created, **kwargs):
# #     if created:
# #         try :
# #             if instance.roll_number:
# #                 Students.Objects.create(user=instance)
# #                 instance.students.save()
            
# #             elif instance.POC:
# #                 StartUps.objects.create(user=instance)
# #                 instance.startups.save()
# #         except:
# #             pass

