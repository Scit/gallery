import os
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.core.exceptions import PermissionDenied


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


def ownership_required(view):
    def wrapped_view(request, *args, **kwargs):
        if request.owner:
            #result = view(request, *args, **kwargs)
            return view(request)
        else:
            raise PermissionDenied

    return wrapped_view
