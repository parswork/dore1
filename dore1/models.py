

from django.db import models
from datetime import datetime

class UserModel(models.Model):
    
    username = models.CharField(max_length=100)
    ncode = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=11)
    rtahsil=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    arr = models.CharField(max_length=100)
   

    def __str__(self):
        return self.username
    


      
        
        
        
      
