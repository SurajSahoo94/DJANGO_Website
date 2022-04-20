from django.db import models

# Create your models here.

class Contact(models.Model):
    name  = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    desc  = models.TextField()
    date  = models.DateTimeField()

# If we want to view the name as contact table directly
    def __str__(self): 
        return self.name

