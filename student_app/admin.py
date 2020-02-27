from django.contrib import admin
from .models import StudentForm

admin.site.register(StudentForm)  #without registring model class name or db table name here after creation of 
                                   #db tables it will not show in DataBase
