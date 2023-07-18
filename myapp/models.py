from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Dataset(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True) # title of the dataset
    description = models.TextField(null=True) # description of the dataset
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'myapp'

class Image(models.Model):
    name = models.CharField(max_length=255)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')