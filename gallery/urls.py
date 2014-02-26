from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'gallery.views.index', name='index'),
    url(r'^(?P<owner_id>\d+)/$', 'gallery.views.owner', name='owner'),
    url(r'^(\d+)/gallery_(?P<gallery_id>\d+)/$', 'gallery.views.gallery', name='gallery'),
    url(r'^(\d+)/gallery_(\d+)/photo_(?P<photo_id>\d+)/$', 'gallery.views.photo', name='photo'),
)
