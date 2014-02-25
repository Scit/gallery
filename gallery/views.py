from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from gallery.models import Gallery
from gallery.utils import paginate


def index(request):
    print "index"
    all_galleries = Gallery.objects.all()
    paginator = paginate(request, all_galleries, count=settings.GALLERIES_ON_PAGE)
    context = {'objects': paginator}
    return render(request, 'gallery/galleries.html', context)


def owner(request, owner_id):
    print "owner"
    try:
        owner = User.objects.get(pk=owner_id)
    except User.DoesNotExist:
        raise Http404

    owners_galleries = Gallery.objects.filter(owner=owner)
    paginator = paginate(request, owners_galleries, count=settings.GALLERIES_ON_PAGE)
    context = {'objects': paginator}
    return render(request, 'gallery/galleries.html', context)


def gallery(request, gallery_id):
    return HttpResponse('%s' % gallery_id)
