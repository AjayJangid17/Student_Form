from django.shortcuts import render, redirect,get_object_or_404
from .forms import StdForm
from .models import StudentForm


# this is main page function which is registration page.
def registration(request):
    student = StdForm       #Form
    if request.method == 'POST':
        student = StdForm(request.POST)
        if student.is_valid():

            formData = student.cleaned_data   #cleaned_data attribute will available after validation of form fields
            data = StudentForm()    #Using fileds from database and written logic to save all data into db.
            data.name = formData['name']
            data.email = formData['email']
            data.gender = formData['gender']
            data.address = formData['address']
            data.city = formData['city']
            data.mobile = formData['mobile']
            data.dob = formData['dob']  
            data.save()
            return redirect(index)      #redirecting to index page
    return render(request,'registration.html',{'student':student})  #this will come up with registration page.


def index(request):

    resultSet = StudentForm.objects.all()       #Fetching all data from DB 

    if 'q' in request.GET and request.GET['q']: #Logic to search a data in table. 
        q = request.GET['q']
        resultSet = resultSet.filter(name__icontains=q)

    return render(request,'index.html',{'resultSet':resultSet}) #this will come up with index page.




def update(request, pk):        # Here pk parameter is stands for (Primary Key) which helps to find choosen data.
    post = get_object_or_404(StudentForm, pk=pk)        #if any error occurs 404 page will pop up insted of any other.
    if request.method == "POST":
        form = StdForm(request.POST, instance=post) 
        if form.is_valid():
            post = form.save(commit=False)
            # post.name = request.name
            post.save()
            return redirect(index)
    else:
        form = StdForm(instance=post)
    return render(request,'update.html',{'form': form})

# Delete Function to delete select data.
def delete(request):
    id = request.GET['id']          
    # select * from StudentForm where id={id}
    result = StudentForm.objects.get(id=id)
    result.delete()
    return redirect(index)
