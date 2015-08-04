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
    url(r'^logout_view/', views.logout_view, name='logout_view'),
    url(r'^logout_successful/', views.logout_successful, name='logout_successful'),


#    url(r'^new_family.html', views.new_family, name='new_family'),
    url(r'^edit_family/(?P<family_id>[0-9]+)/$', views.edit_family,
        name='edit_family'),
    url(r'^edit_camper/(?P<camper_id>[0-9]+)/$', views.edit_camper, name='edit_camper'),

    # url(r'^api_campers/(?P<family_id>[0-9]+)/$', views.api_campers, name='api_campers'),

    # url(r'^dynamic_detail/(?P<family_id>[0-9]+)/$', views.dynamic_detail, name='dynamic_detail'),
    url(r'(?P<family_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^register/$', views.register_view, name='register_view')
#    url(r'(?P<family_id>[0-9]+)/$', views.edit, name='edit'),

    ]
