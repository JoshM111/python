from django.db import models

class dogs(models.Model):
    name= models.CharField(max_length=255)
    age= models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)    
