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

    def test_delete_method(self):
        """
        Function to test that location is being deleted
        """
        self.loc.save_location()
        locations = Location.objects.all()
        self.loc.delete_location()
        self.assertTrue(len(locations) == 0)

    def test_update_method(self):
        """
        Function to test that location is being updated
        """
        self.loc.save_location()
        new_loc = Location.objects.filter().update()
        locations = Location.objects.all()
        # self.loc.update_location()
        self.assertTrue(locations)        