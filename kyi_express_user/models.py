from django.db import models

# Create your models here.

class Kyi_Express_User(models.Model):
    name = models.CharField(max_length=50, blank=False, default="Sender")
    mobile = models.CharField(max_length=25, blank=False, default="Receiver")
    address = models.TextField()
    
