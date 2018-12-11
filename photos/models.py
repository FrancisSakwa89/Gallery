from django.db import models
import datetime as dt
from django.test import TestCase

# Create your models here.

class Location(models.Model):
  location = models.CharField(max_length=60)

  def __str__(self):
    return self.location
  class Meta:
    ordering = ['location']

  def save_location(self):
    self.save()

  def delete_location(self):
    self.delete()

  @classmethod
  def update_location(cls,id,location):
    location = cls.objects.get(pk=id)
    location = cls(location=location)
    location.save()

class PhotosLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Category(models.Model):
  category = models.CharField(max_length=60)

  def __str__(self):
    return self.category
  class Meta:
    ordering = ['category']
    # verbose_name_plural = 'Categories'

  def save_category(self):
    self.save()

  def delete_category(self):
    self.delete()

  @classmethod
  def update_category(cls,id,category):
    category = cls.objects.get(pk=id)
    category = cls(category=category)
    category.save()


class Image(models.Model):
  image = models.ImageField(upload_to = 'photos/')
  name = models.CharField(max_length=60)
  description = models.TextField()
  location = models.ForeignKey(Location)
  Category = models.ManyToManyField(Category)
  pub_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
  class Meta:
    ordering = ['name']

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()
  @classmethod
  def todays_photos(cls):
        today = dt.date.today()
        photos = cls.objects.filter(pub_date__date = today)
        return photos

  @classmethod
  def days_photos(cls,date):
        photos = cls.objects.filter(pub_date__date = date)
        return photos

  @classmethod
  def update_image(cls,id,name,description,location,category):
    image = cls.objects.get(pk=id)
    image = cls(name=name,description=description,location=location,category=category)
    image.save()

  @classmethod
  def get_image_by_id(cls, id):
    image = cls.objects.get(pk=id)
    return image

  @classmethod
  def search_image(cls, search_category_id):
    images = cls.objects.filter(Category=search_category_id)
    return images

  @classmethod
  def filter_by_location(cls, location):
    images = cls.objects.filter(location=location)
    return images

# class photos_image_Category(models.Mode):
#     def photos_image_Category(cls, photos_image_Category):
#         photos_image_Category = cls.objects.filter(photos_image_Category = photos_image_Category)
#         return photos_image_Category


