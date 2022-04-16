from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import FormUserRegistration
# Create your views here.

 


def register(request):
    if request.method=='POST':
        form=FormUserRegistration(request.POST)
        if form.is_valid():
            form.save()
            user_name=form.cleaned_data.get('username')
            messages.success(request, f'Welcome! {user_name}.')
            return redirect('homepage')
            
            
    else:
        form=FormUserRegistration()
    return render(request, "users/register.html", {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('blog-home')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})