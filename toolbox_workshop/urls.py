from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='toolbox_home'),
        path('login/', views.login, name='toolbox_login'),
        path('register/', views.register, name='toolbox_register'),
        path('dashboard/main/', views.dashboard_main, name='toolbox_dashboard_main'),
        path('dashboard/inventory/', views.dashboard_inventory, name='toolbox_dashboard_inventory'),
        path('dashboard/clients/', views.dashboard_clients, name='toolbox_dashboard_clients'),
        path('dashboard/service/', views.dashboard_service, name='toolbox_dashboard_service'),
        path('dashboard/communication/', views.dashboard_communication, name='toolbox_dashboard_communication'),
        path('dashboard/profile/', views.dashboard_profile, name='toolbox_dashboard_profile'),
]
