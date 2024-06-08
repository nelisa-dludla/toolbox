from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='toolbox_home'),
        path('login/', views.login, name='toolbox_login'),
        path('register/', views.register, name='toolbox_register')
]
