from django.db import models

# Create your models here.

class Models(models.Model):
    name = models.CharField(max_length=400)
    image = models.ImageField(null=True, blank=True, upload_to='beta/images/')
    old_price = models.CharField(max_length=400)
    new_price = models.CharField(max_length=400)