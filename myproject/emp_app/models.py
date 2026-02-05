from django.db import models

# Create your models here.

class employee(models.Model):
    name = models.CharField(max_length=30)
    empid = models.CharField(max_length=5)
    dept = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    salary= models.IntegerField(default=0)
    
    def __str__(self):
        return self.name