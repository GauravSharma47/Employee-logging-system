from djongo import models

# Create your models here.
class Employee(models.Model):
    fname=models.CharField(max_length=30)
    mobile=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=30)
    designation=models.CharField(max_length=20)
    time=models.DateTimeField(auto_now=True)
    uId=models.CharField(max_length=15)
    email=models.EmailField(max_length=40)
    pwd=models.CharField(max_length=20)
    empId=models.CharField(max_length=15,primary_key=True)
    loggedIn=models.BooleanField(default=False)
    def __str__(self):
        return self.empId

class Attendance(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    login=models.DateTimeField(auto_now=True)
    logout=models.DateTimeField(null=True)
    
