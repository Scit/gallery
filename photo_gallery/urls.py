from django.conf.urls import patterns, include, url
from django.contrib import admin
import gallery


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photo_gallery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include(gallery.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
