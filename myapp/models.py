
from django.db import models

class Customer(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=10) 

    def __str__(self):
        return self.email
