import os
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def get_upload_path(instance, filename):
    #return u'photos/%s_%s/%s' % (instance.gallery.owner.username,
            #instance.gallery.title, filename)
    return os.path.join('photos', 
                        '%s_%s' % (instance.gallery.owner.username,
                                   instance.gallery.title),
                        filename)


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
