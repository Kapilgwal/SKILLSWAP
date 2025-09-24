from django.db import models

class Registration(models.Model):
    username = models.CharField(max_length=1000,null=False,blank=False,unique=True)
    name = models.CharField(max_length=1000)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.username
