# coding: utf-8
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from gallery.models import Gallery, Photo


class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        exclude = ['owner', 'creation_date']

    def clean(self):
        cleaned_data = self.cleaned_data
        try:
            Gallery.objects.get(owner=self.instance.owner, title=cleaned_data['title'])
        except Gallery.DoesNotExist:
            pass
        else:
            raise ValidationError('Галерея с таким названием уже имеется в вашем альбоме')
        
        return cleaned_data


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ['gallery']

    def __init__(self, *args, **kwargs):
        edit = kwargs.pop('edit', False)
        super(PhotoForm, self).__init__(*args, **kwargs)

        if edit:
            del self.fields['image']
