from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from gallery.models import Gallery, Photo
from gallery.utils import paginate


def index(request):
    all_galleries = Gallery.objects.all()
    paginator = paginate(request, all_galleries, count=settings.GALLERIES_ON_PAGE)
    context = {'objects': paginator}
    return render(request, 'gallery/galleries.html', context)


def owner(request, owner_id):
    try:
        owner = User.objects.get(pk=owner_id)
    except User.DoesNotExist:
        raise Http404

    owners_galleries = Gallery.objects.filter(owner=owner)
    paginator = paginate(request, owners_galleries, count=settings.GALLERIES_ON_PAGE)
    context = {'objects': paginator}
    return render(request, 'gallery/galleries.html', context)


def gallery(request, gallery_id):
    try:
        gallery = Gallery.objects.get(pk=gallery_id)
    except Gallery.DoesNotExist:
        raise Http404

    gallerys_photos = Photo.objects.filter(gallery=gallery)
    paginator = paginate(request, gallerys_photos, count=settings.PHOTOS_ON_PAGE)
    context = {'objects': paginator}
    return render(request, 'gallery/gallery.html', context)


def photo(request, photo_id):
    try:
        photo = Photo.objects.get(pk=photo_id)
    except Photo.DoesNotExist:
        raise Http404

    context = {'photo': photo}
    return render(request, 'gallery/photo.html', context)
