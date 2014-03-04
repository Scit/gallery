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
    image = models.ImageField(upload_to=get_photos_path, verbose_name="Фотография")
    thumbnail_large = models.ImageField(upload_to=get_thumbnails_path, editable=False)
    thumbnail_small = models.ImageField(upload_to=get_thumbnails_path, editable=False)

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    gallery = models.ForeignKey(Gallery, related_name='photos')

    class Meta:
        ordering = ['-pk']

    def save(self):
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile

        thumbnails = (
            ('small', settings.THUMBNAILS_SMALL_SIZE, self.thumbnail_small),
            ('large', settings.THUMBNAILS_LARGE_SIZE, self.thumbnail_large)
        )

        for thumbnail_suffix, thumbnail_size, thumbnail in thumbnails:
            image = Image.open(StringIO(self.image.read()))
            self.image.seek(0)

            if image.mode not in ('L', 'RGB'):
                image = image.convert('RGB')

            image.thumbnail(thumbnail_size, Image.ANTIALIAS)

            handler = StringIO()
            image.save(handler, 'png')
            handler.seek(0)

            suf = SimpleUploadedFile(
                    os.path.split(self.image.name)[-1],
                    handler.read(), content_type='image/png')

            thumbnail.save(u'%s_%s.png' % (suf.name, thumbnail_suffix), suf, save=False)

        super(Photo, self).save()
