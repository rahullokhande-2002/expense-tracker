from django.db import models

class Expenses(models.Model):
    title=models.CharField(max_length=100)
    amoun=models.IntegerField()
    catogery=models.CharField( max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title
