from django.shortcuts import render

def login(request):
    context = {
        'title': 'Login',
    }
    return render(request, 'users/login.html')

def registration(request):
    context = {
        'title': 'Login',
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title': 'Login',
    }
    return render(request, '', context)

def logout(request):
    context = {
        'title': 'Login',
    }
    return render(request, '', context)
# Create your views here.
