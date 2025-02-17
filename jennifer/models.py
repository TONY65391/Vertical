from django.db import models

# Create your models here.

class MODELS(models.Model):
    name = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to= 'jennifer/files/covers', blank=True)