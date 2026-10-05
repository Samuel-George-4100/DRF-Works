from django.db import models

# Create your models here.

class Employee(models.Model):
    empid=models.IntegerField(unique=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)

    gender_choices=[('male','Male'),('female','Female')]# (dbvalue,displayvalue)

    gender=models.CharField(max_length=30,choices=gender_choices)

    joining_date=models.DateField()

    #joined_date=models.DateField(auto_now_add=True)#it adds date value automatically
    #joined_date=models.DateTimeField(auto_now_add=True)#it adds time and date value automatically

    salary=models.IntegerField()
    designation=models.CharField()
    profile_image=models.ImageField(upload_to='profile_picture',null=True)
