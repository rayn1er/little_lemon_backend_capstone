from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField(null=False)

class Booking(models.Model):
    name = models.CharField(max_length=255)
    guest_number = models.IntegerField(null=False)
    booking_date = models.DateTimeField()
