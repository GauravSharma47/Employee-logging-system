from django.shortcuts import render
from django.http import HttpResponse
from register.models import Employee,Attendance
from .forms import loginform

def index(request):
    form=loginform()
    return render(request,'login/index.html',{'form':form})

def logout(request):
    form=loginform()
    return render(request,'login/index.html',{'form':form})


def auth(request):
    uname=request.POST.get('username')
    passd=request.POST.get('password')
    form=loginform()
    try:
        e=Employee.objects.get(empId=uname)
    except:
        return render(request,'login/index.html',{"message":"Please Check your credentials.",'form':form})
    if e.pwd==passd:
        if check_previous_login(e):
            attendance=e.attendance_set.create()
            return render(request,'login/loggedin.html')
        else:
            return render(request,'login/index.html',{"message":"User Already Logged in.",'form':form})
    else:
        return render(request,'login/index.html',{"message":"Please Check your credentials.",'form':form})


def check_previous_login(emp):
    try:
        previous=emp.attendance_set.all()[-1]
        if previous is not None:
            if previous.logouttime==None:
                return True
            else:
                return False
    except:
        return True
