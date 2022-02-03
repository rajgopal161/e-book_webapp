from django.db import models

# Create your models here.

class UserAuth(models.Model):
    def __str__(self):
        return self.username
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    