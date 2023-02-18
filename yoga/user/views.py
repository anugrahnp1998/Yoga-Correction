from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm


def home(request):
    return render(request, 'index.html')

def user_login(request):

    if request.method == 'POST':
       username =  request.POST.get('username')
       password = request.POST.get('password')

       user = authenticate(request, username=username, password=password)
       if user is not None:
            login(request, user)
            return redirect('user_home')
       else:
           messages.info(request, "Username OR Password is incorrect")
           
    context = {}
    return render(request, "login.html", context)




def register(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account has created for '+ user)

            return redirect('login')
            
    context = {'form':form}
    return render(request, "register.html",context)


def user_home(request):
    return render(request, "user_home.html")

