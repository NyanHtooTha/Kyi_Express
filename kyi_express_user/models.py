from django.db import models

# Create your models here.

class Kyi_Express_User(models.Model):
    name = models.CharField(max_length=50, blank=False)
    mobile = models.CharField(max_length=25, blank=False)
    address = models.TextField()
    
