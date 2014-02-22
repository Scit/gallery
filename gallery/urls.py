from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'gallery.views.index', name='index'),
)
