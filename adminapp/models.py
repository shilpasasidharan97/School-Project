from datetime import datetime
from distutils.command.upload import upload
import email
from django.db import models

# Create your models here.

class TeacherBasic(models.Model):
    t_id=models.AutoField(primary_key=True)
    t_profile=models.ImageField(upload_to='teachers/')
    t_name=models.CharField(max_length=20)
    gender=models.CharField(max_length=7)
    dob=models.DateField()
    age=models.IntegerField()
    religion=models.CharField(max_length=15)
    cast=models.CharField(max_length=10)
    place=models.CharField(max_length=20)
    district=models.CharField(max_length=20,default="")
    nationality=models.CharField(max_length=20)
    aadhar_num=models.IntegerField()
    email_id=models.CharField(max_length=25)
    phone_number=models.IntegerField()
    handling_class=models.IntegerField()
    subject=models.CharField(max_length=15)
    qualification=models.CharField(max_length=30)
    college_name=models.CharField(max_length=50)
    quali_certificate=models.FileField(upload_to='teachers/')
    instituation_name=models.CharField(max_length=50)
    year_of_experience=models.IntegerField()
    experience_certificate=models.FileField(upload_to='teachers/')

    class Meta:
        db_table='teachers'


