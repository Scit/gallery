from django.db import models
from django.contrib.auth.models import User
from gallery.utils import get_upload_path


class Gallery(models.Model):
    owner = models.ForeignKey(User, related_name='galleries')
    creation_date = models.DateTimeField()
    title = models.CharField(max_length=100)

    class Meta:
        unique_together = ('owner', 'title')
        ordering = ['-creation_date']


class Photo(models.Model):
    file = models.ImageField(upload_to=get_upload_path)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    gallery = models.ForeignKey(Gallery, related_name='photos')
