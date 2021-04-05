from rest_framework import serializers
from .models import *

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        ordering = ('created', )
        fields = ['id','ticketPrice','customerName','creationDate','perfomanceTitle','perfomanceTime']
