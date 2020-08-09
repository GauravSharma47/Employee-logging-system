from djongo import models

# Create your models here.
class Employee(models.Model):
    _id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50)
    mobile=models.CharField(max_length=14)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    time=models.DateTimeField(auto_now=True)
    uId=models.CharField(max_length=15)
    email=models.CharField(max_length=40)
    pwd=models.CharField(max_length=100)
    empId=models.CharField(max_length=50)
    def __str__(self):
        return self._id
