from ..models import *
from ..viewsets import *
from ..serializers import *
from rest_framework.test import APIClient,APITransactionTestCase,APITestCase
from django.db import connections
from rest_framework import status

# Create your tests here.

#granted create db to our user so he can create test db

class testServerWorking(APITestCase):
    def test_server_working(self):
        url='http://127.0.0.1:8000/university/Address/'
        response=self.client.get(url)
        #content=json.loads(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
class TestAddress(APITransactionTestCase):
    
    reset_sequences = True
    
    #TODO : talk about setup classmethod
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_add_address(self):
        data={
            "street": "new_street",
            "city": "new_city",
            "adrs": "numero 256",
            "zip_code": 2080
        }
        url='http://127.0.0.1:8000/university/Address/'
        addresses=address.objects.count()
        # a verif
        self.assertEqual(addresses,0)
        response=self.client.post(url,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED) # 201 for successfuly created
        self.assertEqual(response.data['street'],"new_street")
        n=address.objects.count()
        self.assertEqual(n,addresses+1)
        
    
    def test_get_adrs_by_id(self):
        """
        test for valid id 
        """
        adr=address.objects.create(street= "new_street",
            city= "new_city",
            adrs= "numero 256",
            zip_code= 3081)
        response=self.client.get(f'http://127.0.0.1:8000/university/Address/{adr.id}/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['zip_code'],3081)
        
    
    def test_get_adrs_by_invalid_id(self):
        """
        provide invalid id
        """
        response=self.client.get(f'http://127.0.0.1:8000/university/Address/-5/')
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND) # not found
        
    def test_get_all_adresses(self):
        adrs1=address.objects.create(street= "this street",
        city= "this city",
        adrs= "this adrs",
        zip_code= 1000)
        
        adrs2=address.objects.create(street= "this street",
        city= "this city",
        adrs= "this adrs",
        zip_code= 1001)
        
        response=self.client.get('http://127.0.0.1:8000/university/Address/')
        self.assertEqual(response.data[0]["zip_code"],adrs1.zip_code)
        self.assertEqual(response.data[1]["zip_code"],adrs2.zip_code)
    
    def test_delete_address(self):
        #just to show how to work with api client insted of client of the class
        clt=APIClient()
        adrs1=address.objects.create(street= "this street",
        city= "this city",
        adrs= "this adrs",
        zip_code= 1000)
        #verifier existant
        response=clt.get(f'http://127.0.0.1:8000/university/Address/{adrs1.id}/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data["zip_code"],1000)
        #deleting this adrs
        response_delete=clt.delete(f'http://127.0.0.1:8000/university/Address/{adrs1.id}/')
        response_list=clt.get('http://127.0.0.1:8000/university/Address/')
        response_adrs1=clt.get(f'http://127.0.0.1:8000/university/Address/{adrs1.id}/')
        #check if delete went okkkkkkkk
        #200 or 204 both are correct I guess  haseb stackoverflow
        self.assertEqual(response_delete.status_code,status.HTTP_204_NO_CONTENT)
        # get list adrss went okay 
        self.assertEqual(response_list.status_code,status.HTTP_200_OK)
        # to check len of list after delete should return to 0
        self.assertEqual(len(response_list.data),0)
        # get by id the adrs we deleted shouldnt work
        self.assertEqual(response_adrs1.status_code,status.HTTP_404_NOT_FOUND) # id shouldnt be found 
    
    def test_delete_adrs_with_invalid_id(self):
        response=self.client.delete(f'http://127.0.0.1:8000/university/Address/-1000/')
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
        
    #we should test the put method cuz its integrated in ourviewset methods
    def test_update_adrs(self):
        adrs1=address.objects.create(street= "this street",
        city= "this city",
        adrs= "this adrs",
        zip_code= 1000)
        response=self.client.put(f'http://127.0.0.1:8000/university/Address/{adrs1.id}/',{
            "street": "new_street",
            "city": "this city",
            "adrs": "this adrs",
            "zip_code": 2080
        })
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['street'],"new_street")
        self.assertEqual(response.data['city'],"this city")
        self.assertEqual(response.data['adrs'],"this adrs")
        self.assertEqual(response.data['zip_code'],2080)
        
        #try to get the user and verify again
        response_adrs1=self.client.get(f'http://127.0.0.1:8000/university/Address/{adrs1.id}/')
        self.assertEqual(response_adrs1.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['street'],"new_street")
        self.assertEqual(response.data['city'],"this city")
        self.assertEqual(response.data['adrs'],"this adrs")
        self.assertEqual(response.data['zip_code'],2080)
        
    def test_update_adrs_wrong_id(self):
        response=self.client.put(f'http://127.0.0.1:8000/university/Address/-1000/',{
            "street": "new_street",
            "city": "this city",
            "adrs": "this adrs",
            "zip_code": 2080
        })
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
        
    def test_update_adrs_with_invalid_data(self): # provide invalid json
        adrs1=address.objects.create(street= "this street",
        city= "this city",
        adrs= "this adrs",
        zip_code= 1000)
        
        response=self.client.put(f'http://127.0.0.1:8000/university/Address/{adrs1.id}/',{
            "name": "azerty",
            "descr": "lakzejalj",
        },
        content_type="application/json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST) #400 server cannot proceed lput ly amalneha
        
        
