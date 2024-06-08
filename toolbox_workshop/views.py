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

def dashboard_main(request):
    context = {
        'title': 'Main Dashboard'
    }
    return render(request, 'toolbox_workshop/dashboard_main.html', context=context)

def dashboard_inventory(request):
    context = {
        'title': 'Inventory Management'
    }
    return render(request, 'toolbox_workshop/dashboard_inventory.html', context=context)

def dashboard_clients(request):
    context = {
        'title': 'Clients'
    }
    return render(request, 'toolbox_workshop/dashboard_clients.html', context=context)

def dashboard_service(request):
    context = {
        'title': 'Service Records'
    }
    return render(request, 'toolbox_workshop/dashboard_service.html', context=context)

def dashboard_communication(request):
    context = {
        'title': 'Communication'
    }
    return render(request, 'toolbox_workshop/dashboard_communication.html', context=context)

def dashboard_profile(request):
    context = {
        'title': 'Profile'
    }
    return render(request, 'toolbox_workshop/dashboard_profile.html', context=context)
