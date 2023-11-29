from django.db import models


# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname + "" + self.lastname


class Destinations(models.Model):
    Image = models.ImageField(upload_to='images/')
    dname = models.CharField(max_length=50)
    eprice = models.IntegerField(default=0)
    description = models.TextField()
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.dname
