from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.



class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField

#    opening_bid = models.DecimalField(max_digits=7, decimal_places=2, default=1.00)

    def __str__(self):
        return self.name

class Auction(models.Model):
    auction_start_date = models.DateTimeField(auto_now_add=True) #put in item?
    auction_end_date = models.DateTimeField() #default=timezone.now? datetime.datetime.now()?
#    winner = models. # FK to bid?
#     opening_bid = models.ForeignKey(Item)
    opening_bid = models.DecimalField(max_digits=7, decimal_places=2, default=1.00)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    item = models.ForeignKey(Item)
#    bids = models.ManyToOne???
    increment = models.DecimalField(max_digits=7, decimal_places=2, default=1.00)
    auction_ended = models.BooleanField(default=False)




    def __str__(self):
        return self.item.name


    # def ended(self):
    #     if self.auction_end_date < datetime.datetime.now():
    #         self.auction_ended = True
    #         return self.auction_ended

    # def set_winner(self):
    #     if self.auction_ended == True:
    #         self.winner = max bid self


    # def bid(self):
    #     if self.bid.max_bid > self.bid:
    #         self.bid = self.bid.max_bid
    #         self.price = self.increment + self.bid
    #         return self.price

    # def number_of_bids(self):
    #     bids = Bid.objects.filter(id=auction_id)
    #     number_of_bids = bids.length()


class Bid(models.Model):
    auction = models.ForeignKey(Auction)
    bidder = models.ForeignKey(User)
    bid_amount = models.DecimalField(max_digits=7, decimal_places=2, default=1.00)

    class Meta:
        ordering = ['bid_amount', ]
