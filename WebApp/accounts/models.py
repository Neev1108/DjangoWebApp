from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Type is checking or savings
class Account(models.Model):
    customer = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add = True)
    type = models.CharField(max_length = 1, default= None)
    
    

    def toString(self):
        type = self.type
        if self.type == "S":
            type = "Savings"
        else:
            type = "Checking"
        return "$" + str(self.balance) + " | " + type
    

