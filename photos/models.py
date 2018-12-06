from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length = 60)    
    
    def __str__(self):
        return self.location
    class Meta:
        ordering = ['location']
    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()
    def update_location(self):
        self.update()


class Image(models.Model):
  image = models.ImageField(upload_to = 'photos/')
  name = models.CharField(max_length=60)
  description = models.TextField()
  location = models.ForeignKey(Location,on_delete=models.CASCADE)
  category = models.ManyToManyField('category')
  

  def __str__(self):
    return self.name
  class Meta:
    ordering = ['name']

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

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
class Category(models.Model):
  category = models.CharField(max_length=60)

  def __str__(self):
    return self.category
  class Meta:
    ordering = ['category']

  def save_category(self):
    self.save()

  def delete_category(self):
    self.delete()

  @classmethod
  def update_category(cls,id,category):
    category = cls.objects.get(pk=id)
    category = cls(category=category)
    category.save()