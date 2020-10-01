from django.db import models

class Show(models.Model):
    title= models.CharField(max_length=48)
    network= models.CharField(max_length=24)
    release= models.CharField(max_length=24)
    desc= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
