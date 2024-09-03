from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=10)
    message=models.TextField()

    def __str__(self):
        return self.name

class Destination(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    placename=models.CharField(max_length=100)
    cityname=models.CharField(max_length=100)
    hotelname=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class TicketBooking(models.Model):
    urcity=models.CharField(max_length=789)
    todest=models.CharField(max_length=122)
    day=models.CharField(max_length=122)
    seats=models.CharField(max_length=122)
    message=models.TextField()

    def __str__(self):
        return f"{self.urcity} to {self.todest}"
