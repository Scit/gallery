from django.shortcuts import render
from django.http import HttpResponse
from gallery.models import Gallery
from gallery.utils import paginate


def index(request):
    all_galleries = Gallery.objects.all()
    paginator = paginate(request, all_galleries, count=2)
    context = {'objects': paginator}
    return render(request, 'gallery/galleries.html', context)


def owner(request, ):
    pass


def gallery(request, gallery_id):
    return HttpResponse('%s' % gallery_id)
