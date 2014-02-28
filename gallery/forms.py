from django.forms import ModelForm
from gallery.models import Gallery, Photo


class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        exclude = ['owner', 'creation_date']


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ['gallery']
