"""super_simple_auction URL Configuration

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
from auction import views

urlpatterns = [
    url(r'^auction/', include('auction.urls', namespace='auction')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^login.html$', views.login_view, name="login"),
    url(r'^register.html$', views.register_view, name="register"),
    url(r'^add_item.html$', views.add_item, name="add_item"),
    url(r'^add_auction/(?P<item_id>[0-9]+)/$', views.add_auction, name="add_auction"),
    url(r'^auction_detail/(?P<auction_id>[0-9]+)$', views.auction_detail, name="auction_detail"),
]
