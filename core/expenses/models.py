from django.db import models
from django.contrib.auth.models import User


class Expenses(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)    
    title=models.CharField(max_length=100)
    amoun=models.IntegerField()
    catogery=models.CharField( max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title



