from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length = 60)    

    def __str__(self):
        return self.location
    class Meta:
        ordering = ['location']

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    location = models.ForeignKey(Location,)
    # category = models.ManyToManyField(Category)

class Category(models.Model):
    category = models.CharField(max_length=60)
    def __str__(self):
        return self.category
    class Meta:
        ordering = ['category']    