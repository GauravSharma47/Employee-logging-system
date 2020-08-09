from django.shortcuts import render
from django.http import HttpResponse
from register.models import Employee
from .forms import loginform

def index(request):
    form=loginform()
    return render(request,'login/index.html',{'form':form})

def auth(request):
    uname=request.POST.get('uname')
    passd=request.POST.get('paswd')
    e=Employee.objects.filter(empId=uname).filter(pwd=passd)
    if len(e)==1:
        return render(request,'login/loggedin.html')
    else:
        return render(request,'login/index.html',{"message":"Please Check your credentials."})
