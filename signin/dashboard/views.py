from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from app2.form2 import RegisterForm  # reuse the same form

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'DashBoard/user_list.html', {'users': users})

@login_required
def user_edit(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            if 'password' in form.cleaned_data:
                user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'User updated successfully.')
            return redirect('user_list')
    else:
        form = RegisterForm(instance=user)
    return render(request, 'dashboard/user_edit.html', {'form': form, 'user': user})

@login_required
def user_delete(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('user_list')
