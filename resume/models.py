from django.db import models
import datetime

# Create your models here.

class Userinfo(models.Model):
    UserId=models.AutoField
    image=models.ImageField(upload_to='user/passport', default=" ")
    Name=models.CharField(max_length=100,default=" ")
    Designation=models.CharField(max_length=50, default=" ")
    phone=models.IntegerField(default="0")
    Altphone=models.IntegerField(default="0")
    email=models.EmailField(max_length=50,default=" ")
    Address=models.CharField(max_length=100,default=" ")
    Dist=models.CharField(max_length=100,default=" ")
    pincode=models.IntegerField(default="0")
    skill=models.CharField(max_length=100,default=" ")
    skillSecond=models.CharField(max_length=100,default=" ")
    skillThird=models.CharField(max_length=100,default=" ")
    skillFour=models.CharField(max_length=100,default=" ")
    skillFive=models.CharField(max_length=100,default=" ")
    CareerObjective=models.TextField(default='')
    Degree=models.CharField(max_length=100,default=" ")
    DegreePassingYear=models.DateField()
    DegreeBranch=models.CharField(max_length=100,default=" ")
    Degreeinstitude=models.CharField(max_length=100)
    DegreeCGPA=models.CharField(max_length=20, default=" ")
    Degreepercent=models.IntegerField(default="0")
    HSC=models.CharField(max_length=100)
    HSCPassingYear=models.DateField()
    HSCBranch=models.CharField(max_length=100)
    HSCinstitude=models.CharField(max_length=100)
    HSCpercent=models.IntegerField(default="0")
    HSCCGPA=models.CharField(max_length=20, default=" ")
    # Scc
    SCCYear=models.DateField()
    SCCinstitude=models.CharField(max_length=100)
    SCCpercent=models.IntegerField(default="0")
    # Certificate
    CertificateName=models.CharField(max_length=100)
    CourceName=models.CharField(max_length=100)
    CourceDate=models.DateField()
    # project
    ProjectTitle=models.CharField(max_length=100)
    ProjectName=models.CharField(max_length=100)
    ProjectDate=models.DateField()
    ProjectStatus=models.CharField(max_length=20,default=" ")
    # Experiance
    CompanyName=models.CharField(max_length=50, default=" ")
    JobDesignation=models.CharField(max_length=50, default=" ")
    JobDescription=models.TextField( default=" ")
    JobStart=models.DateField()
    Present=models.CharField(max_length=20)
    JobSend=models.DateField(default= datetime.date.today)
    def __str__(self):
        return self.Name