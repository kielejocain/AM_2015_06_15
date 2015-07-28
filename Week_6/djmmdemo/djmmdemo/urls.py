from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/all/get/$', 'djmmdemo_app.views.api_get', name='api_get'),
    url(r'^api/v1/all/post/$', 'djmmdemo_app.views.api_post', name='api_post'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.contrib.staticfiles.views',
        url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'djmmdemo_app/index.html'}),
        url(r'^(?P<path>(?:js|css|img)/.*)$', 'serve'),
    )
