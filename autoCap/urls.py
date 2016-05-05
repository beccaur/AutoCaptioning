from django.conf.urls import include, url
from django.contrib import admin

from images.views import index, tests, report

from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'autoCap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^tests.html', tests),
    url(r'^report.html', report),
    url(r'^media/(?P<path>.*)$', {'document_root':settings.MEDIA_ROOT})
]
