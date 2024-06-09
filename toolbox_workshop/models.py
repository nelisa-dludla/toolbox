from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=128, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Record(models.Model):
    id = models.AutoField(primary_key=True)
    service_rendered = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
