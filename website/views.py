from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Record
from .forms import AddRecordForm



# Create your views here.

def home(request):

    records = Record.objects.all()


    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate here
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been to login!")
            return redirect('home')
        else:
            messages.success(request, "Please try again")
            return redirect('home')
    else:
         return render(request, 'home.html', {'records': records})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "you have been logout")
    return redirect('home')

def customer_record(request, pk):
    #take this primary and return record
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "you must be login to see this page")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "you must be login to see this page")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    print(request)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "you must be login to add record")
        return redirect('home')


