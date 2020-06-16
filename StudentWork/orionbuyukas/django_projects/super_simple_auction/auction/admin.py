from django.contrib import admin
from models import Auction, Bid, Item
# Register your models here.
admin.site.register(Item)
admin.site.register(Auction)
admin.site.register(Bid)
