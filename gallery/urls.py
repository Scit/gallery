from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'gallery.views.index', name='index'),
    url(r'^(?P<owner_id>\d+)/$', 'gallery.views.owner', name='owner'),
    url(r'^(\d+)/(?P<gallery_id>\d+)/$', 'gallery.views.gallery', name='gallery'),
)
