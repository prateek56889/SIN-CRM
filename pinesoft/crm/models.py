from django.db import models
class clients(models.Model):
    created_by=models.CharField(max_length=100,default="NULL")
    branch=models.CharField(max_length=100,default="NULL")
    name=models.CharField(max_length=100,default="NULL")
    father_name=models.CharField(max_length=100,default="NULL")
    spouse_name=models.CharField(max_length=100,default="NULL")
    DOB=models.CharField(max_length=1000,default="NULL")
    aadhar=models.CharField(max_length=1000,default="NULL")
    PAN=models.CharField(max_length=1000,default="NULL")
    Address=models.CharField(max_length=1000,default="NULL")
    pincode=models.CharField(max_length=100,default="NULL")
    price_quoted=models.CharField(max_length=100,default="NULL")
    query=models.CharField(max_length=1000,default="NULL")
    Remarks=models.CharField(max_length=100,default="NULL")
    Status=models.CharField(max_length=100,default="NULL")
    approved=models.CharField(max_length=100,default="NULL")
class usr(models.Model):
    name=models.CharField(max_length=100,default="NULL")
    branch=models.CharField(max_length=100,default="NULL")

class Notification(models.Model):
    name=models.CharField(max_length=100,default="NULL")
    info=models.CharField(max_length=100,default="NULL")
    time=models.DateTimeField(auto_now=True)



