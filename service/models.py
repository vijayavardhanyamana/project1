from django.db import models
class login1(models.Model):
    selectoption=models.CharField(max_length=10)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    
class profilepatient(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    bloodgroup=models.CharField(max_length=5,null = True)
    email=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    phone=models.CharField(max_length=50,null = True)
    dateofbirth=models.CharField(max_length=30,null = True)
    address=models.CharField(max_length=1000,null = True)
    
    

    
    
    
# Create your models here.
