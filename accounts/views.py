from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect('product_list')
            else:
                messages.error(request, 'Username already exist')

        else:
            messages.error('Both username and password are required.')

    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('product_list')