

from django.db import models
from datetime import datetime

class UserModel(models.Model):
    
    username = models.CharField(max_length=100,unique=True)
    ncode = models.CharField(max_length=10,unique=True)
    phonenumber = models.CharField(max_length=11,unique=True)
    rtahsi=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    arr = models.CharField(max_length=100)
   

    def __str__(self):
        return self.username
    


      
        
        
        
      
