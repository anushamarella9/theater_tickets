from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
import uuid

# Create your views here.

class CreateTicketView(APIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    uid = uuid.uuid4().hex
    authentication_classes = (authentication.TokenAuthentication, )

    def post(self,request):
        ticketPrice = request.POST.get('ticketPrice')
        customerName = request.POST.get('customerName')
        creationDate = request.POST.get('creationDate')
        perfomanceTitle = request.POST.get('perfomanceTitle')
        perfomanceTime = request.POST.get('perfomanceTime')
        
        serializer = TicketSerializer(data=request.POST)
        if not serializer.is_valid():
            return Response(serializer.errors,status=400)

        signup = Ticket.objects.create(ticketPrice=ticketPrice,customerName=customerName,
        	creationDate=creationDate,perfomanceTitle=perfomanceTitle,perfomanceTime=perfomanceTime)
        
        return json({"message":"success"},status=201)

class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class UpdateTicketView(APIView):
    uid = uuid.uuid4().hex

    authentication_classes = (authentication.TokenAuthentication, )

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def put(self, request,*args, **kwargs):

        request_data = self.request.data
        print("request.data")
        print(self.request.data)
        updated_coupon = Ticket.objects.all()

        ticket_id = self.kwargs['ticket_id']
        ticketPrice = request.POST.get('ticketPrice')
        customerName = request.POST.get('customerName')
        perfomanceTitle = request.POST.get('perfomanceTitle')

        try:
            updated_ticket = Ticket.objects.get(id=ticket_id)
            updated_ticket.ticketPrice = ticketPrice
            updated_ticket.customerName = customerName
            updated_ticket.perfomanceTitle = perfomanceTitle
            updated_ticket.save()

        except Ticket.DoesNotExist:
            return Response("errors")

        return Response({"ticket has been updated"},updated_ticket)

class TicketDeleteView(APIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    uid = uuid.uuid4().hex
    authentication_classes = (authentication.TokenAuthentication, )

    def delete(self, *args, **kwargs):
        queryset = Ticket.objects.all()

        ticket_id = self.kwargs['ticket_id']

        coupons = Ticket.objects.filter(id=ticket_id).delete()

        return Response({"message":"Ticket deleted successfully"},status=200)