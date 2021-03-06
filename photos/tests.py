from django.test import TestCase
from .models import Location, Category, Image
import datetime as dt

# Create your tests here.

class LocationTestClass(TestCase):
    """
    Tests Location class and its functions
    """
    #Set up method
    def setUp(self):
        self.loc = Location()

    def test_instance(self):
        self.assertTrue(isinstance(self.loc, Location))

    def test_save_method(self):
        self.loc.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) >0)   

    def test_delete_method(self):
        self.loc.save()
        self.loc.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)
    
    def test_update_method(self):
        """
        Function to test that a location's details can be updates
        """
        self.loc.save_location()
        new_place = Location.objects.filter().update()
        locations = Location.objects.get()
        self.assertTrue(locations)


class CategoryTestClass(TestCase):
    """
    Tests category class and its functions
    """
    #Set up method
    def setUp(self):
        self.cat = Category()
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))
    
    def test_save_method(self):
        """
        Function to test that category is being saved
        """
        self.cat.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        """
        Function to test that a category can be deleted
        """
        self.cat.save_category()
        self.cat.delete_category()

    def test_update_method(self):
        """
        Function to test that a category's details can be updated
        """
        self.cat.save_category()
        new_cat = Category.objects.filter().update()
        categories = Category.objects.get()
        self.assertTrue(categories)


class ImageTestClass(TestCase):
    """
    Tests Image class and its functions
    """
    #Set up method
    def setUp(self):
        #creating a new location and saving it
        self.loc = Location()
        self.loc.save_location()

        #creating a new category and saving it
        self.cat = Category()
        self.cat.save_category()

        #creating an new image 
        self.image = Image(location=self.loc)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        """
        Function to test an image and its details is being saved
        """
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        """
        Function to test if an image can be deleted
        """
        self.image.save_image()
        self.image.delete_image()

    def test_update_method(self):
        """
        Function to test that an image's details can be updates
        """
        self.image.save_image()
        new_image = Image.objects.filter().update()
        images = Image.objects.get()
        self.assertTrue(images)

    def test_get_image_by_id(self):
        """
        Function to test if you can get an image by its id
        """
        self.image.save_image()
        my_img= self.image.get_image_by_id(self.image.id)
        image = Image.objects.get(id=self.image.id)
        self.assertTrue(my_img, image)

    def test_filter_by_location(self):
        """
        Function to test if you can get an image by its location
        """
        self.image.save_image()
        my_img = self.image.filter_by_location(self.image.location)
        image = Image.objects.filter(location=self.image.location)
        self.assertTrue(my_img, image)

    # def test_filter_by_category_name(self):
    #     """
    #     Function to test if you can get an image by its category name
    #     """
    #     self.image.save_image()
    #     this_img = self.image.filter_by_category(self.image.Category)
    #     images = Image.search_image('my')
    #     self.assertTrue(len(images)>0)

    def test_get_photos_today(self):
        today_photos = Image.todays_photos()
        # self.assertTrue(len(today_photos)>0)

    def test_get_photos_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        photos_by_date = Image.days_photos(date)
        self.assertTrue(len(photos_by_date) == 0) 