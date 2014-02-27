from django.forms import ModelForm
from gallery.models import Gallery


class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        exclude = ['owner', 'creation_date']
