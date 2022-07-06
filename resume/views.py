import imp
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from resume.models import *

# Create your views here.
def index(request):
    return(render(request,'resume/index.html'))

def create(request):
    if request.method == "POST":
        D=Userinfo()
        D.image=request.FILES['images']
        D.Name=request.POST['Name']
        D.Designation=request.POST['Designation']
        D.phone=request.POST['phone']
        D.Altphone=request.POST['Altphone']
        D.email=request.POST['email']
        D.Address=request.POST['Address']
        D.skill=request.POST['skill']
        D.skillSecond=request.POST['skillSecond']
        D.skillThird=request.POST['skillThird']
        D.skillFour=request.POST['skillFour']
        D.skillFive=request.POST['skillFive']
        D.CareerObjective=request.POST['CareerObjective']
        D.Degree=request.POST['Degree']
        D.DegreePassingYear=request.POST['DegreePassingYear']
        D.DegreeBranch=request.POST['DegreeBranch']
        D.Degreeinstitude=request.POST['Degreeinstitude']
        D.Degreepercent=request.POST['Degreepercent']
        D.HSC=request.POST['HSC']
        D.HSCPassingYear=request.POST['HSCPassingYear']
        D.HSCBranch=request.POST['HSCBranch']
        D.HSCinstitude=request.POST['HSCinstitude']
        D.HSCpercent=request.POST['HSCpercent']
        D.SCCYear=request.POST['SCCYear']
        D.SCCinstitude=request.POST['SCCinstitude']
        D.SCCpercent=request.POST['SCCpercent']
        D.CertificateName=request.POST['CertificateName']
        D.CourceName=request.POST['CourceName']
        D.CourceDate=request.POST['CourceDate']
        D.ProjectTitle=request.POST['ProjectTitle']
        D.ProjectName=request.POST['ProjectName']
        D.ProjectDate=request.POST['ProjectDate']
        D.ProjectStatus=request.POST['ProjectStatus']
        D.CompanyName=request.POST['CompanyName']
        D.JobDesignation=request.POST['JobDesignation']
        D.JobDescription=request.POST['JobDescription']
        D.Present=request.POST['Present']
        D.JobStart=request.POST['JobStart']
        D.JobSend=request.POST['JobEnd']
        D.save()
        Data=Userinfo.objects.all().last
        params={'Data':Data}
        print(Data)
        return(render(request,'Resume/create.html', params))
    Data=Userinfo.objects.all().last
    params={'Data':Data}
    return(render(request,'Resume/create.html',params))
    # return(render(request,'resume/create.html'))
