from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photo_gallery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('gallery.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^register/$', 'photo_gallery.views.register', name='register'),
)
