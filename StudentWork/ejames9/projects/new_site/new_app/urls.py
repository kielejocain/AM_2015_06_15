"""new_site URL Configuration

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
from new_app import views
from django.contrib.auth.models import User

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^blog/(?P<id>[0-9]+)/$', views.details, name='details'),
    url(r'^edit/(?P<id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^create2/(?P<id>[0-9]+)/$', views.create2, name='create2'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^api_delete_comment/', views.api_delete_comment, name='details'),


]
