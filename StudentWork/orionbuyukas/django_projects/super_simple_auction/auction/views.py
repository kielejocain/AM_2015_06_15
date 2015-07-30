from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect, get_object_or_404
from models import Auction, Bid, Item

# Create your views here.
def index(request):
    auctions = Auction.objects.order_by('-auction_end_date')
    return render(request, 'index.html', {'auctions': auctions})


# def bid(request, auction_id, user_id ):
#    # auction = get_object_or_404(Auction, pk=auction_id)
#     if request == "POST":
#         max_bid = request.POST['max_bid']
#         bid = Bid()
#         bid.bidder = user_id
#         bid.bid_amount = max_bid
#         bid.save()
#     return render(request, 'auction/auction_id', {"auction": bid})

def add_item(request):
    if request == "POST":
        item = Item()
        item.name = request.POST['item_name']
        item.description = request.POST['description']
        # item.opening_bid = request.POST['opening_bid']
        item.save()
        return redirect('add_auction.html', {'item': item})
    return render(request, 'add_item.html', {})

def add_auction(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request == "POST":
        auction = Auction()
        auction.item = item
        auction.opening_bid = request.POST['opening_bid']
        auction.auction_end_date = request.POST['auction_end_date']
        auction.increment = request.POST['increment']
        auction.save()
        return redirect('auction/auction_detail/', {'auction': auction})
    return render(request, 'add_auction.html', {})   #{'item': item}

def auction_detail(request, auction_id):
    auction = get_object_or_404(Item, pk=auction_id)
    bids = Bid.objects.filter(id=auction_id)
    if bids[0] > auction.price:
        auction.price += auction.increment
        auction.save()
    elif auction.price < auction.opeing_bid:
        auction.price = auction.opening_bid
        auction.save()

        return render(request, 'auction_detail.html', {'auction': auction})






def bid(request, user_id, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)
    # bids = Bid.objects.filter(id=auction_id)
    if request == "POST":
        bid = Bid()
        bid.bidder = user_id
        bid.bid_amount = request.POST['bid_amount']
        bid.save()
        return render(request, 'auction_detail.html', {'auction': auction})




