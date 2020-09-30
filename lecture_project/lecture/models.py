from django.db import models
class Dragon(models.Model):
    name = models.CharField(max_length=45)
    has_wings = models.BooleanField()
    fire_color = models.CharField(max_length=45)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Geocache(models.Model):
    location = models.CharField(max_length=30)
    treasure = models.TextField()
    dragon = models.ForeignKey(Dragon, related_name="owned_geocaches", on_delete = models.CASCADE)
    dragons_that_found = models.ManyToManyField(Dragon, related_name="found_geocaches")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
