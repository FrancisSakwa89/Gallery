from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

class Location(models.Model):
    location = models.CharField(max_length = 60)    

    def __str__(self):
        return self.location
    class Meta:
        ordering = ['location']