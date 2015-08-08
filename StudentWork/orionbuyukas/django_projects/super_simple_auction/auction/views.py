from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect, get_object_or_404
from models import Auction, Bid, Item
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")

    return render(request, 'login.html', {})


def register_view(request):
    if request.POST:
        user = User()
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.set_password(request.POST['password'])
        user.save()
        return HttpResponseRedirect("/login/")

    return render(request, 'register.html', {})

def check_user_auth(user):
    if user.is_authenticated():
        return True
    else:
        return False



def index(request):
    auctions = Auction.objects.order_by('-auction_end_date')

    return render(request, 'index.html', {'auctions': auctions, 'user_login': check_user_auth(request.user)})


# def bid(request, auction_id, user_id ):
#    # auction = get_object_or_404(Auction, pk=auction_id)
#     if request == "POST":
#         max_bid = request.POST['max_bid']
#         bid = Bid()
#         bid.bidder = user_id
#         bid.bid_amount = max_bid
#         bid.save()
#     return render(request, 'auction/auction_id', {"auction": bid})

@login_required(login_url='/login/')
def add_item(request):
    if request.POST:
        item = Item()
        item.name = request.POST['item_name']
        item.description = request.POST['description']
        item.seller = request.user
        item.save()
      #  url = reverse('add_auction', kwargs={ 'item_id': item.id })

        return HttpResponseRedirect(reverse('auction:add_auction', args=(item.id,)))
    return render(request, 'add_item.html', {})

@login_required(login_url='/login/')
def add_auction(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.POST:
        auction = Auction()
        auction.item = item

        auction.opening_bid = request.POST['opening_bid']
        auction.auction_end_date = request.POST['auction_end_date']
        auction.increment = request.POST['increment']
        auction.save()
        return HttpResponseRedirect(reverse('auction:auction_detail', args=(auction.id,)))
    return render(request, 'add_auction.html', {'item_id': item_id})

def auction_detail(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)

    bids = Bid.objects.filter(id=auction_id)

    if len(bids) < 1:
        print("NO BIDS!")
        if auction.price < auction.opening_bid:
            auction.price = auction.opening_bid
            auction.save()

    else:
        bid = bids[0]
        if bid.amount > auction.price:
            auction.price += auction.increment
            auction.save()

    return render(request, 'auction_detail.html', {'auction': auction})



@login_required(login_url='/login/')
def bidding(request, user_id, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)
    # bids = Bid.objects.filter(id=auction_id)
    if request == "POST":
        bid = Bid()
        bid.bidder = user_id
        bid.bid_amount = request.POST['bid_amount']
        bid.save()
        return render(request, 'auction_detail.html', {'bid': bid})
    return render(request, 'bidding.html', {{'auction': auction}})



