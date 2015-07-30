from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class AdminSettings(models.Model):
    small_size_threshold = models.IntegerField(max_length=4, default=20)
    medium_size_threshold = models.IntegerField(max_length=4, default=150)

class RegUser(models.Model):
    Bio = models.TextField
    zipcode = models.IntegerField(max_length=10)


class Studio(models.Model):
    studio_name = models.CharField(max_length=250)
    user = models.ForeignKey(RegUser)
    blog = models.ForeignKey(Blog)
    products = models.ForeignKey(Item)


class Blog(models.Model):
    blog_text = models.TextField
    pub_date = models.DateTimeField(auto_now_add=True)
    studio = models.ForeignKey(Studio)

class Auction(models.Model):
    auction_description = models.TextField
    auction_start_date = models.DateTimeField(auto_now_add=True) #put in item?
    auction_end_date = models.DateTimeField() #timedelta add default time of now?
    winner = models.ForeignKey(Bids)
    opening_bid = models.ForeignKey(Item)
    item = models.ForeignKey(Item)
    bids = models.ForeignKey(Bids)
    increment = models.DecimalField(max_digits=7, decimal_places=2, default=1.00)


    def ending_soon(self):
        dif = self.auction_end_date - datetime.datetime.now()
        if dif.days < datetime.timedelta(days=1):  # divide to get hours?
            return "<Ending Soon!> %d days" % dif.days

    def was_published_recently(self):
        return self.pub_date <= timezone.now() - datetime.timedelta(days=1)

class Bids(models.Model):
    auction = models.ForeignKey(Auction)
    bidder = models.ForeignKey(RegUser)
    max_bid = models.DecimalField(max_digits=15, decimal_places=2, default=1.00)
    bid_amount = models.DecimalField(max_digits=15, decimal_places=2, default=1.00)
    price = models.DecimalField

    def bid(self):
        if self.bid_amount > self.max_bid:
            self.price += self.increment
            return self.price

class Order(models.Model):
    item = models.ForeignKey(Auction)

    fulfilled = models.BooleanField(default=False)

class Item(models.Model):

    item_name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField(default=1)
    #price = models.ForeignKey(Auction)
    opening_bid = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    height_cm = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    width_cm = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    depth_cm = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    weight_grams = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    small_size_threshold = models.ForeignKey(AdminSettings)
    medium_size_threshold = models.ForeignKey(AdminSettings)


    def __str__(self):
        return self.item_name


    def size_calc(self):


        if self.height_cm < self.small_size_threshold and self.width_cm < self.small_size_threshold and self.depth_cm < self.small_size_threshold:
            size = "Small"
        elif self.height_cm < self.medium_size_threshold and self.width_cm < self.medium_size_threshold and self.depth_cm < self.medium_size_threshold :
            size = "medium"
        else:
            size = "Large"
        return size

