from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'gallery.views.index', name='index'),
    url(r'^(?P<owner_id>\d+)/$', 'gallery.views.owner', name='owner'),
    url(r'^(?P<owner_id>\d+)/add/$', 'gallery.views.gallery_edit', name='gallery_edit'),

    url(r'^(?P<owner_id>\d+)/gallery_(?P<gallery_id>\d+)/$', 'gallery.views.gallery', name='gallery'),
    url(r'^(?P<owner_id>\d+)/gallery_(?P<gallery_id>\d+)/add/$', 'gallery.views.photo_edit', name='photo_add'),
    url(r'^(?P<owner_id>\d+)/gallery_(?P<gallery_id>\d+)/delete/$', 'gallery.views.object_delete', name='object_delete'),

    url(r'^(?P<owner_id>\d+)/gallery_(?P<gallery_id>\d+)/photo_(?P<photo_id>\d+)/$', 'gallery.views.photo', name='photo'),
    url(r'^(?P<owner_id>\d+)/gallery_(?P<gallery_id>\d+)/photo_(?P<photo_id>\d+)/edit/$', 'gallery.views.photo_edit', name='photo_edit'),
    url(r'^(?P<owner_id>\d+)/gallery_(?P<gallery_id>\d+)/photo_(?P<photo_id>\d+)/delete/$', 'gallery.views.object_delete', name='object_delete'),

    url(r'^(?P<owner_id>\d+)/gallery_(?P<gallery_id>\d+)/photo_(?P<photo_id>\d+)/comment_(?P<comment_id>\d+)/delete/$', 'gallery.views.comment_delete', name='comment_delete'),

    url(r'^comments/posted/$', 'gallery.views.comment_posted', name='comment_posted'),
    url(r'^comments/', include('django.contrib.comments.urls')),
)
