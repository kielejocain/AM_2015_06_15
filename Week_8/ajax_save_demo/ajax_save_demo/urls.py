from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'ajax_save_app.views.index', name='index'),
                       url(r'^api/v1/model/$', 'ajax_save_app.views.api_model', name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
