from django.shortcuts import render, redirect
from .models import reigister
from .form import registerForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def register(request):
    form=registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:
            return render(request, 'register.html', {'form': form, 'error': 'Invalid data. Please correct the errors below.'})
    return render(request, 'register.html', {'form': form})

def login_view(request):
    return HttpResponse("Login Page")
def user_details(request):
    data = reigister.objects.all()
    return render(request, 'details.html', {'data': data})
    
