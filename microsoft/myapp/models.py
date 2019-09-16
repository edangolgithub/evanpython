from __future__ import unicode_literals  
from django.db import models  


class Employee(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  

class Student(models.Model):  
        first_name = models.CharField(max_length=20)  
        last_name  = models.CharField(max_length=30)  
        contact    = models.IntegerField()  
        email      = models.EmailField(max_length=50)  
        age        = models.IntegerField() 
class Employee1(models.Model):  
    eid      = models.CharField(max_length=20)  
    ename    = models.CharField(max_length=100)  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee1"  

  
class Student1(models.Model):  
    first_name = models.CharField(max_length=20)  
    last_name  = models.CharField(max_length=30)  
    class Meta:  
        db_table = "student1" 