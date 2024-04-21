from django.db import models

# Create your models here.
class carausel(models.Model):
    title = models.CharField('title', max_length=250)
    sub_title = models.CharField('sub_title', max_length=250)
    docu = models.FileField(upload_to='images/', max_length=255 )

class card1(models.Model):
    title = models.CharField('title', max_length=250)
    sub_title = models.CharField('sub_title', max_length=250)
    docu = models.FileField(upload_to='images/', max_length=255 )

class card2(models.Model):
    title = models.CharField('Dr. Name', max_length=50)
    sub_title = models.CharField('sub_title', max_length=50)
    docu = models.FileField(upload_to='images/', max_length=255 )

class appointment(models.Model):
    yourname = models.CharField(max_length=50)
    youraddress = models.CharField(max_length=50)
    emailaddress = models.CharField(max_length=50)
    yourage = models.CharField(max_length=25)
    Date = models.DateField()
    Time = models.CharField(max_length=20, null=True)
    Doctor = models.CharField(max_length=50, null=True)

class contact(models.Model):
    memail = models.CharField(max_length=50)
    mphone = models.CharField(max_length=25)
    maddress = models.CharField(max_length=50)
    mcity = models.CharField(max_length=50)
    mstate = models.CharField(max_length=50)
    mpinno = models.CharField(max_length=25)
    mdetails = models.CharField(max_length=50)

