from django.db import models

# Create your models here.

class AWB(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    awb_number = models.CharField(max_length=25, blank=False, default='')    
    sender = models.ForeignKey('kyi_express_user.Kyi_Express_User', on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey('kyi_express_user.Kyi_Express_User', on_delete=models.CASCADE, related_name="receiver")
    
    class Meta:
        ordering = ('created',)
        
    