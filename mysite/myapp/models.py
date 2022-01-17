from django.db import models

# Create your models here.


class Book(models.Model):
    
    #This function is used for object representation (Which displays the object name)
    def __str__(self):
        return self.Name

    Name = models.CharField(max_length=100)
    Desc = models.CharField(max_length=300)
    Price = models.IntegerField()
    image = models.ImageField(default="default.png", upload_to="book_images/")

