"""seabeck_draft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from my_app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^login_needed/', views.login_needed, name='login_needed'),

#    url(r'^new_registrant.html', views.new_registrant, name='new_registrant'),
    url(r'^edit_registrant/(?P<registrant_id>[0-9]+)/$', views.edit_registrant,
        name='edit_registrant'),
    url(r'^edit_camper/(?P<camper_id>[0-9]+)/$', views.edit_camper, name='edit_camper'),

    url(r'^api_campers/(?P<registrant_id>[0-9]+)/$', views.api_campers, name='api_campers'),

    url(r'^dynamic_detail/(?P<registrant_id>[0-9]+)/$', views.dynamic_detail, name='dynamic_detail'),
    url(r'(?P<registrant_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^register/$', views.register_view, name='register_view')
#    url(r'(?P<registrant_id>[0-9]+)/$', views.edit, name='edit'),

    ]
