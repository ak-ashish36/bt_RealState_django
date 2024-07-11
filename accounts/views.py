from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
       #REGISTER USER
       messages.error(request ,'Testing error message' )
       return redirect('register')
    return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
       #LOGIN USER
       messages.error(request ,'Testing error message' )
       return redirect('login')
    return render(request,'accounts/login.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def logout(request):
    return redirect('')
