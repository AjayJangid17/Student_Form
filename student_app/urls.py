from django.urls import path
from student_app import views

urlpatterns = [
    path('',views.registration,name='register'),
    path('index',views.index,name='index'),
    path('delete',views.delete),
    path('update/<int:pk>/',views.update,name='update'), #Here int will convert (string) pk into interger. 
   
]
