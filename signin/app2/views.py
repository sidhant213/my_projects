from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .form2 import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful. Please login.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'app2/register.html', {'form': form})

