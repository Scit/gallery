from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'gallery.views.index', name='index'),
    url(r'^(?P<owner_id>\d+)/$', 'gallery.views.owner', name='owner'),
    url(r'^(?P<owner_id>\d+)/add/$', 'gallery.views.gallery_edit', name='gallery_edit'),

    url(r'^(?P<owner_id>\d+)/gallery_(?P<gallery_id>\d+)/$', 'gallery.views.gallery', name='gallery'),

    url(r'^(?P<owner_id>\d+)/gallery_(?P<gallery_id>\d+)/photo_(?P<photo_id>\d+)/$', 'gallery.views.photo', name='photo'),

    url(r'^comments/', include('django.contrib.comments.urls')),
)
