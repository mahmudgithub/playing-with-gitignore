from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=100)
    city =models.CharField(max_length=50)
    roll=models.IntegerField()
    Images=models.ImageField()

    def __str__(self):
        return self.name

