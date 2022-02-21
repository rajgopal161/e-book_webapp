from django.db import models

# Create your models here.

class Cart(models.Model):
    def __str__(self):
        return self.usrid
    usrid = models.IntegerField()
    prodid = models.IntegerField()
    quantity = models.IntegerField()