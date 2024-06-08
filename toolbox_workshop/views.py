from django.shortcuts import render

def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'toolbox_workshop/home.html', context=context)

def login(request):
    context = {
        'title': 'Login'
    }
    return render(request, 'toolbox_workshop/login.html', context=context)

def register(request):
    context = {
        'title': 'Register'
    }
    return render(request, 'toolbox_workshop/register.html', context=context)
