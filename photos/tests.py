from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.
class LocationTestClass(TestCase):
    """
    Tests Location class and its functions
    """
    #Set up method
    def setUp(self):
        self.loc= Location('Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.loc, Location))