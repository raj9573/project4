from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.models import userprofile

def home(request):

    if request.method == 'POST':
        print("post method is getting activated")

        name =  request.POST['name']
        age = request.POST['age']

        print(name,age)

        userprofile.objects.create(name=name,age=age)

        return HttpResponse("data inserted successfully")

    return render(request,'home.html')

    # return HttpResponse("home page")

def display(request):

    User_details = userprofile.objects.all()
        

    return render(request,'display.html',context={'User_details':User_details})

