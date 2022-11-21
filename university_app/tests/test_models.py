from django.test import TestCase , RequestFactory,SimpleTestCase
from ..models import *

class test_university(TestCase):
    def setUp(self):
        University.objects.create(name='ISGT',location='Bardo')
        #University.objects.create(name='IHEC',location='Carthage')
        
    def test_univ_obj(self):
        isg=University.objects.get(name='ISGT')
        self.assertEqual(isg.location,'Bardo')
        self.assertIsInstance(isg.location,str) # verify que loc est une chaine de char