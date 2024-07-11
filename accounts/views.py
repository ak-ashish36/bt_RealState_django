from django.shortcuts import render,redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
       #REGISTER USER
       return
    return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
       #LOGIN USER
       return
    return render(request,'accounts/login.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def logout(request):
    return redirect('')
