from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'registration_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'registration_app.views.index'),
    url(r'^login/$', 'registration_app.views.login_view'),
    url(r'^register/$', 'registration_app.views.register_view'),
    url(r'^admin/', include(admin.site.urls)),
)
