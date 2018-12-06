from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.
class LocationTestClass(TestCase):
    """
    Tests Location class and its functions
    """
    #Set up method
    def setUp(self):
        self.loc= Location()

    def test_instance(self):
        self.assertTrue(isinstance(self.loc, Location))

    def test_save_method(self):
        """
        Function to test that location is being saved
        """
        self.loc.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)    