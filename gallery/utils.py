import os
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def get_photos_path(instance, filename):
    return os.path.join(settings.PHOTOS_MEDIA_ROOT,
            '%s_%s' % (instance.gallery.owner.pk,
            instance.gallery.pk), filename)


def get_thumbnails_path(instance, filename):
    return os.path.join(settings.THUMBNAILS_MEDIA_ROOT,
            '%s_%s' % (instance.gallery.owner.pk,
            instance.gallery.pk), filename)

            
def paginate(request, objects, count=10, param_name='page'):
    paginator = Paginator(objects, count)

    try:
        pagenum = int(request.GET.get('%s' % param_name, '1'))
    except ValueError:
        pagenum = 1

    try:
        result = paginator.page(pagenum)
    except (EmptyPage, InvalidPage):
        result = paginator.page(paginator.num_pages)

    return result
