from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def create_validator(self, reqPOST):#reqPOST is the request.POST data from the views.py file but named differently here because request.POST isnt a usable variable
        errors= {}
        # add keys and values to errors dict for each invalid field
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
                                    # in the email reg the ^ is the start point 
                                    # the $ is the end
                                    # the pluses allow any number of characters as long as they are the within the confines of the arguement symbols
        if len(reqPOST['user_name']) < 5:
            errors['user_name']= "Name must be at least 5 characters."
        if len(reqPOST['email']) < 8:
            errors['email']= "Email needs to be longer."
        if len(reqPOST['password']) < 8:
            errors['password']= "Password must be at least 8 characters."
        if reqPOST['password'] != reqPOST['password_conf']:
            errors['password_conf']= "Passwords must match!"
        if not EMAIL_REGEX.match(reqPOST['email']):
            errors['regex']= "Email is not in the correct format."
        return errors
class KoalaManager(models.Manager):
    def create_validator(self, reqPOST):
        errors={}
        if len(reqPOST['koala_name']) < 3:
            errors['koala_name']= "Name should be at least 3 characters"
        if len(reqPOST['talent'])> 6:
            errors['talent']= "Koalas are more talented than that!"
        koala_with_same_name= Koala.objects.filter(name=reqPOST['koala_name'])
        if len(koala_with_same_name) > 0:
            errors['duplicate'] = "Name has already been taken, try again."
        return errors



# EACH CLASS SHOULD HAVE ITS OWN MANAGER TO MAKE EDITS

class User(models.Model):
    name= models.CharField(max_length=24)
    email= models.CharField(max_length=48)
    password= models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects= UserManager()

class Koala(models.Model):
    name= models.CharField(max_length=40)
    talent= models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(User, related_name="koalas", on_delete=models.CASCADE)
    users_vote= models.ManyToManyField(User, related_name="koala_votes")
    objects= KoalaManager()