from django.db import models

class User(models.Model):
    name= models.CharField(max_length=24)
    email= models.CharField(max_length=48)
    password= models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)