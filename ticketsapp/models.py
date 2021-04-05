from django.db import models

# Create your models here.
class Ticket(models.Model):
	ticketPrice = models.DecimalField(max_digits=5,decimal_places=2)
	customerName = models.CharField(max_length=50)
	creationDate = models.DateField(auto_now=True)   
	perfomanceTitle = models.CharField(max_length=100)
	perfomanceTime = models.TimeField(auto_now=True)