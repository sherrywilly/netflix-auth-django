from django.contrib.auth import authenticate, get_user_model, login, logout
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from accounts.models import User

User = get_user_model()
def  index(request):
    return HttpResponse("Hello, world. You're at the accounts index.")
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(email=username).first()
        if user is not None:
            if user.is_active:
                if user.check_password(password):
                    login(request, user)
                return redirect(reverse('accounts:dash'))
            else:
                return redirect(reverse('accounts:login'))
        else:
            return redirect(reverse('accounts:login'))
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        password2 =    request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                return render(request, 'accounts/signup.html', {'error': 'Email already exists'})
            else:
                user = User.objects.create_user(email=email, password=password)
                user.save()
                return redirect(reverse('accounts:login'))

        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords do not match'})
        
    return render(request, 'accounts/signup.html')

def logout_view(request):
    logout(request)
    return render(request, 'accounts/login.html')