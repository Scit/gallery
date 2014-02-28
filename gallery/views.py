# coding: utf-8
import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
from gallery.models import Gallery, Photo
from gallery.forms import GalleryForm, PhotoForm
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


def photo(request, *args, **kwargs):
    photo_id = kwargs.get('photo_id', None)
    try:
        photo = Photo.objects.get(pk=photo_id)
    except Photo.DoesNotExist:
        raise Http404

    context = {'photo': photo}
    return render(request, 'gallery/photo.html', context)


@ownership_required
def gallery_edit(request, *args, **kwargs):
    if request.POST:
        owner_id = kwargs.get('owner_id', None)
        owner = get_object_or_404(User, pk=owner_id)

        gallery = Gallery(owner=owner, creation_date=datetime.datetime.now())
        form = GalleryForm(request.POST, instance=gallery)
        if form.is_valid():
            form.save()

            redirect_url = reverse('owner', args=(owner_id,))
            return HttpResponseRedirect(redirect_url)
    else:
        form = GalleryForm()

    context = {'form': form}
    return render(request, 'gallery/gallery_edit.html', context)


@ownership_required
def photo_edit(request, *args, **kwargs):
    owner_id = kwargs.get('owner_id', None)
    gallery_id = kwargs.get('gallery_id', None)
    gallery = get_object_or_404(Gallery, pk=gallery_id)
    photo_id = kwargs.get('photo_id', None)

    if photo_id:
        edit = True
        photo = get_object_or_404(Photo, pk=photo_id)

    else:
        edit = False
        photo = Photo(gallery=gallery)

    if request.POST:
        form = PhotoForm(request.POST, instance=photo, edit=edit)
        if form.is_valid():
            form.save()

            redirect_url = reverse('gallery', args=(owner_id, gallery_id))
            return HttpResponseRedirect(redirect_url)
    else:
        form = PhotoForm(instance=photo, edit=edit)

    context = {'form': form}
    return render(request, 'gallery/photo_edit.html', context)


@ownership_required
def object_delete(request, *args, **kwargs):
    owner_id = kwargs.get('owner_id', None)
    gallery_id = kwargs.get('gallery_id', None)
    photo_id = kwargs.get('photo_id', None)

    if photo_id:
        context = {'notification': u'Удаление фотографии %s' % photo_id}
    elif gallery_id:
        context = {'notification': u'Удаление галереи %s' % gallery_id}

    if request.POST:
        if photo_id:
            Photo.objects.get(pk=photo_id).delete()

            redirect_url = reverse('gallery', args=(owner_id, gallery_id,))
            return HttpResponseRedirect(redirect_url)
        elif gallery_id:
            Gallery.objects.get(pk=gallery_id).delete()

            redirect_url = reverse('owner', args=(owner_id,))
            return HttpResponseRedirect(redirect_url)

    else:
        return render(request, 'gallery/object_delete.html', context)
