from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Employee
from django.utils import timezone
from django.contrib import messages
from random import randint

def index(request):
    return render(request,'register/index.html',None)

def check_value(num,val):
    # Returns True if Number not found in Db
    try:
        if num ==1:
            Employee.objects.get(mobile=val)
        elif num==2:
            Employee.objects.get(uId=val)
        else:
            Employee.objects.get(empId=val)
        return False
    except:
        return True

def getId(name,city):
    id=name[:3]+str(randint(1000,9999))+city[:3]
    while check_value(3,id) is False:
        id=name[:3]+str(randint(1000,9999))+city[:3]
    return id




def submitDetails(request):
    if request.method=='POST':
        name=request.POST.get('fname');number=request.POST.get('mobile');city=request.POST.get('city')
        state=request.POST.get('state');desig=request.POST.get('designation');aadhar=request.POST.get('uId')
        email=request.POST.get('mail');pwd=request.POST.get('pwd')
        time=timezone.now()
        if check_value(1,number) and check_value(2,aadhar):
            empid=getId(name,city)
            e=Employee(fname=name,mobile=number,city=city,state=state,designation=desig,time=time,uId=aadhar,email=email,pwd=pwd,empId=empid)
            e.save()
            context={"Name":name,"message":"Registration Successful!","empid":empid}
            return render(request,'register/registered.html',context)
        else:
            return render(request,'register/index.html',{"message":"User Already Registered"})
    else:
        return render(request,'register/index.html',{"message":"'Internal Error! Please Try Again'"})
