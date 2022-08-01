from django.db import models

# Create your models here.

# Creates a data packet with name and timestamp that can be accessed from shell
class Name(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)  # Timestamp
