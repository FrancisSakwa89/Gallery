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

class CategoryTestClass(TestCase):
    """
    Tests category class and its functions
    """
    #Set up method
    def setUp(self):
        self.cat = Category(name='this', description='testing pic')
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
        Function to test that a category's details can be updates
        """
        self.cat.save_category()
        new_cat = Category.objects.filter(name='calm').update(name='good')
        categories = Category.objects.get(name='good')
        self.assertTrue(categories.name, 'good')


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
        self.cat = Category(name='calm', description='test2')
        self.cat.save_category()

        #creating an new image 
        self.image = Image(photo='come.jpg', name='name', description = 'calm photo', location=self.locale, category = self.cat)

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
        new_image = Image.objects.filter(photo='come.jpg').update(photo='good.jpg')
        images = Image.objects.get(photo='good.jpg')
        self.assertTrue(images.photo, 'good.jpg')

    def test_get_image_by_id(self):
        """
        Function to test if you can get an image by its id
        """
        self.image.save_image()
        this_img= self.image.get_image_by_id(self.image.id)
        image = Image.objects.get(id=self.image.id)
        self.assertTrue(this_img, image)

    def test_filter_by_location(self):
        """
        Function to test if you can get an image by its location
        """
        self.image.save_image()
        this_img = self.image.filter_by_location(self.image.location)
        image = Image.objects.filter(location=self.image.location)
        self.assertTrue(this_img, image)

    def test_filter_by_category_name(self):
        """
        Function to test if you can get an image by its category name
        """
        self.image.save_image()
        images = Image.search_image('this')
        self.assertTrue(len(images)>0)