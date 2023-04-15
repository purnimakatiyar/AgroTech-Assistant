from django.db import models

# Create your models here.
class Sgn(models.Model):
    username = models.CharField(max_length=122)
    fname = models.CharField(max_length=122)
    lname = models.CharField(max_length=122)
    email = models.EmailField()
    address = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.username
    
class Suppsgn(models.Model):
    username = models.CharField(max_length=122)
    fname = models.CharField(max_length=122)
    lname = models.CharField(max_length=122)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.username
    
class SupplierOrder(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    crop_name = models.CharField(max_length=122)
    crop_quantity = models.CharField(max_length=122)
    address = models.TextField()
    city = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    zip = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name