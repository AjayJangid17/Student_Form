from django import forms
from student_app.models import StudentForm

class StdForm(forms.ModelForm):
    
    class Meta:
        model = StudentForm     #usnig db fields
        fields = '__all__'      #here calling all db tables to display with help of tamplates(html file).