from django.test import TestCase , RequestFactory,SimpleTestCase,TransactionTestCase
from ..models import *
from ..viewsets import *
from ..serializers import *
from rest_framework.test import APIClient,APITestCase,APITransactionTestCase
from django.contrib.auth.models import User ,AnonymousUser
import json
from django.urls import reverse, resolve
from http import HTTPStatus
from django.db import connections

# address serializer
class testAddress(TestCase):
    def test_valid_serializer(self):
        valid_data={
            "street": "new_street",
            "city": "new_city",
            "adrs": "numero 256",
            "zip_code": 2080
        }
        serializer=addressSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data,valid_data)
        self.assertEqual(serializer.data,valid_data)
        self.assertEqual(serializer.errors,{})
        
    def test_invalid_serializer(self):
        invalid_data={
            "street": "",
            "city":"",
            "adrs": "numero 256",
            "zip_code": "2080abc"
        }
        serializer=addressSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid()) #it should be false
        # we cant user validated data without using is_valid
        self.assertEqual(serializer.validated_data,{}) # should be empty cuz andna 2 champs neksyn w champ type data ghalt
        self.assertEqual(serializer.data,invalid_data)
        #print(serializer.errors)
        self.assertEqual(serializer.errors,{"street":["This field may not be blank."],"city":["This field may not be blank."],"zip_code":["A valid integer is required."]})
        
        