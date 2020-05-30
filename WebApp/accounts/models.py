from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Type is checking or savings
class Account(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    date_created = models.DateTimeField(auto_now_add = True)
    
    
    
    def toString(self):
        return self.first_name + " " + self.last_name
    

