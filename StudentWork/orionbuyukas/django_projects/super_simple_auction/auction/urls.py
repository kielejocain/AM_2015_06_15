from django.conf.urls import include, patterns, url
from django.contrib import admin
from auction import views


urlpatterns = [
    url(r'^login.html$', views.login_view, name="login"),
    url(r'^register.html$', views.register_view, name="register"),
    url(r'^add_item.html$', views.add_item, name="add_item"),
    url(r'^(?P<item_id>[0-9]+)/add_auction.html$', views.add_auction, name="add_auction"),
    url(r'^(?P<auction_id>[0-9]+)/auction_detail.html$', views.auction_detail, name="auction_detail"),
    url(r'^(?P<auction_id>[0-9]+)/bidding.html$', views.bidding, name="bidding"),
]
