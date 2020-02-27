from django.db import models
import datetime


class StudentForm(models.Model):

    #this all fields will create in database with powefull concept of ORM
    name = models.CharField(max_length=100, null=True, default=None)
    email = models.CharField(max_length=100, unique=True,default=None)
    gender = models.CharField(max_length=10, null=True, default=None)
    address = models.TextField(null=True, default=None)
    city = models.CharField(max_length=250, null=True, default=None)
    mobile = models.IntegerField(null=True, default=None)
    dob = models.DateTimeField(default=None,auto_now=False, auto_now_add=False)

    def __str__(self):      #this function will helps in converting into string 
        return self.name     # in database rows pop up with names     
        
    class Meta:

        db_table = 'Student Form' #db table name

    
    