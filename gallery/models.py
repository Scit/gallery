# coding: utf-8
import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from gallery.utils import get_photos_path, get_thumbnails_path


class Gallery(models.Model):
    owner = models.ForeignKey(User, related_name='galleries')
    creation_date = models.DateTimeField()
    title = models.CharField(max_length=100)

    class Meta:
        unique_together = ('owner', 'title')
        ordering = ['-creation_date']

    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.owner.username)


class Photo(models.Model):
    image = models.ImageField(upload_to=get_photos_path)
    thumbnail_large = models.ImageField(upload_to=get_thumbnails_path, editable=False)
    thumbnail_small = models.ImageField(upload_to=get_thumbnails_path, editable=False)

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    gallery = models.ForeignKey(Gallery, related_name='photos')

    def save(self):
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile

        image = Image.open(StringIO(self.image.read()))
        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')

        #image_copy = image.copy()

        thumbnail_small = image.resize(settings.THUMBNAILS_SMALL_SIZE, Image.ANTIALIAS)
        thumbnail_large = image.resize(settings.THUMBNAILS_LARGE_SIZE, Image.ANTIALIAS)

        thumbnails = (
            ('small', thumbnail_small, self.thumbnail_small),
            ('large', thumbnail_large, self.thumbnail_large)
        )

        for thumbnail_suffix, thumbnail_image, thumbnail in thumbnails:
            handler = StringIO()
            thumbnail_image.save(handler, 'png')
            handler.seek(0)

            suf = SimpleUploadedFile(
                    os.path.split(self.image.name)[-1],
                    handler.read(), content_type='image/png')

            thumbnail.save(u'%s_%s.png' % (suf.name, thumbnail_suffix), suf, save=False)

        super(Photo, self).save()
