from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User

from ticketsapp.models import *

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status
from django.db.models import Q
import uuid

class AddTicketTest(TestCase):

    def test_add_ticket(self):
    	uid = uuid.uuid4().hex
    	response = self.client.get('api/v1/tickets/createticket/', data={
            'ticketPrice':"150",
            'customerName' : "abc",
            'perfomanceTitle': "title1",
            "creationDate": "2021-04-05",
        	"perfomanceTime": "11:05:58.447071"
           })
    	print('response****************',response)
    	self.assertEqual(response.status_code,201)

    def test_add_ticket2(self):
    	uid = uuid.uuid4().hex
    	response = self.client.post('api/v1/tickets/createticket/', data={
            'ticketPrice':"anusha",
            'customerName' : "abc",
            'perfomanceTitle': "title1",
            "creationDate": "2021-04-05",
        	"perfomanceTime": "11:05:58.447071"
           })
    	print('response',response)
    	self.assertEqual(response.status_code,201)

    def test_add_ticket3(self):
    	uid = uuid.uuid4().hex
    	response = self.client.post('api/v1/tickets/createticket/', data={
            'ticketPrice':"anusha",
            'customerName' : "123#453",
            'perfomanceTitle': "title1",
            "creationDate": "2021-04-05",
        	"perfomanceTime": "11:05:58.447071"
           })
    	print('response',response)
    	self.assertEqual(response.status_code,201)


    def test_add_ticket4(self):
    	uid = uuid.uuid4().hex
    	response = self.client.post('api/v1/tickets/createticket/', data={
            'ticketPrice':"anusha",
            'customerName' : "abc",
            'perfomanceTitle': "12$eg4xt",
            "creationDate": "2021-04-05",
        	"perfomanceTime": "11:05:58.447071"
           })
    	print('response',response)
    	self.assertEqual(response.status_code,201)
    def test_add_ticket5(self):
    	uid = uuid.uuid4().hex
    	response = self.client.post('api/v1/tickets/createticket/', data={
            'ticketPrice':"anusha",
            'customerName' : "123#453",
            'perfomanceTitle': "title1",
            "creationDate": "2021",
        	"perfomanceTime": "11:05:58.447071"
           })
    	print('response',response)
    	self.assertEqual(response.status_code,201)


    def test_add_ticket6(self):
    	uid = uuid.uuid4().hex
    	response = self.client.post('api/v1/tickets/createticket/', data={
            'ticketPrice':"anusha",
            'customerName' : "abc",
            'perfomanceTitle': "12$eg4xt",
            "creationDate": "2021-04-05",
        	"perfomanceTime": "11"
           })
    	print('response',response)
    	self.assertEqual(response.status_code,201)

