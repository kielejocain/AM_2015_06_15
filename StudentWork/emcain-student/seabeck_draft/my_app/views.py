from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.core.urlresolvers import reverse

from django.shortcuts import get_object_or_404, render

from .models import Registrant, Camper, Rate

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def login_needed(request):
#     template = loader.get_template('seabeck_draft/login_needed.html')
#     return render(template, 'seabeck_draft/login_needed.html', {})
#


def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")

    return render(request, 'seabeck_draft/login.html', {})


def register_view(request):

    if request.POST:
        user = User()
        user.username = request.POST['username']
        user.email = request.POST['username']
        user.set_password(request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()

        registrant = Registrant()
        registrant.user = user
        registrant.phone = request.POST['phone']
        registrant.save()

        camper = Camper()
        camper.registrant = registrant
        camper.first_name = user.first_name
        camper.last_name = user.last_name
        camper.under_18 = False
        camper.dob = None
        camper.save()

        return HttpResponseRedirect("/login/")

    return render(request, 'seabeck_draft/register.html', {})


def logout_view(request):
    logout(request)
    # Redirect to a success page.

@login_required(login_url='/login_needed/')
def index(request):
    registrants_list = Registrant.objects.order_by("user__last_name")
#often use two underscores to represent dot/fk relationship
    template = loader.get_template('seabeck_draft/index.html')
    context = RequestContext(request, {'registrants_list': registrants_list})

    return HttpResponse(template.render(context))

@login_required()
def detail(request, registrant_id):
    registrant = get_object_or_404(Registrant, pk=registrant_id)
    return render(request, 'seabeck_draft/detail.html', {'registrant': registrant})


def login_needed(request):
    return render(request, 'seabeck_draft/login_needed.html')

def edit_registrant(request, registrant_id):

    if registrant_id == 0:
        print "new"
        registrant = Registrant()
    else:
        print "existing"
        registrant = get_object_or_404(Registrant, pk=registrant_id)

    filtered_registrant_list = Registrant.objects.filter(id=registrant_id)

#    if len(filtered_registrant_list) > 0:
    registrant = filtered_registrant_list[0]
#    else:
#        registrant = Registrant()

    if request.POST:
        print(request.POST)
        registrant.first_name = request.POST["first_name"]
        registrant.last_name = request.POST["last_name"]
        registrant.email = request.POST["email"]
        registrant.phone = request.POST["phone"]
        registrant.save()
        return HttpResponseRedirect("/")

    return render(request, 'seabeck_draft/edit_registrant.html', {'registrant': registrant})


def new_registrant(request):

    registrant = Registrant()

    if request.POST:
        print(request.POST)
        registrant.first_name = request.POST["first_name"]
        registrant.user.last_name = request.POST["user.last_name"]
        registrant.email = request.POST["email"]
        registrant.phone = request.POST["phone"]
        registrant.save()
        return HttpResponseRedirect("/")

    return render(request, 'seabeck_draft/new_registrant.html', {'registrant': registrant})


def edit_camper(request, camper_id):

    if camper_id == "0":
        camper = Camper()
    else:
        camper = get_object_or_404(Camper, pk=camper_id)

    filtered_camper_list = Camper.objects.filter(id=camper_id)

    if len(filtered_camper_list) > 0:
        camper = filtered_camper_list[0]
    else:
        camper = Camper()

    if request.POST:
        print(request.POST)
        camper.first_name = request.POST["first_name"]
        camper.last_name = request.POST["last_name"]
        camper.under_18 = request.POST["under_18"]
        camper.save()
        return HttpResponseRedirect("/")

    return render(request, 'seabeck_draft/edit_camper.html', {'camper': camper})
