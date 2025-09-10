from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('logout')  # Redirect to logout view after login
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'app1/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'app1/logout.html')
