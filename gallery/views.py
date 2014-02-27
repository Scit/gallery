from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from gallery.models import Gallery, Photo
from gallery.utils import paginate, ownership_required


def index(request):
    all_galleries = Gallery.objects.all()
    paginator = paginate(request, all_galleries, count=settings.GALLERIES_ON_PAGE)
    context = {'objects': paginator}
    return render(request, 'gallery/galleries.html', context)


def owner(request, *args, **kwargs):
    owner_id = kwargs.get('owner_id', None)

    try:
        owner = User.objects.get(pk=owner_id)
    except User.DoesNotExist:
        raise Http404

    owners_galleries = Gallery.objects.filter(owner=owner)
    paginator = paginate(request, owners_galleries, count=settings.GALLERIES_ON_PAGE)
    context = {'objects': paginator}
    return render(request, 'gallery/galleries.html', context)


def gallery(request, *args, **kwargs):
    gallery_id = kwargs.get('gallery_id', None)
    try:
        gallery = Gallery.objects.get(pk=gallery_id)
    except Gallery.DoesNotExist:
        raise Http404

    gallerys_photos = Photo.objects.filter(gallery=gallery)
    paginator = paginate(request, gallerys_photos, count=settings.PHOTOS_ON_PAGE)
    context = {'objects': paginator}
    return render(request, 'gallery/gallery.html', context)


@ownership_required
def gallery_add(request, *args, **kwargs):
    return HttpResponse('ok')


def photo(request, *args, **kwargs):
    photo_id = kwargs.get('photo_id', None)
    try:
        photo = Photo.objects.get(pk=photo_id)
    except Photo.DoesNotExist:
        raise Http404

    context = {'photo': photo}
    return render(request, 'gallery/photo.html', context)