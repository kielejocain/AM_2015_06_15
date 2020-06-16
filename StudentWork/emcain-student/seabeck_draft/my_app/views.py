from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.core.urlresolvers import reverse

from django.shortcuts import get_object_or_404, render, redirect

from .models import Family, Camper, Rate, EventYear, Attendance

import json

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

        family = Family()
        family.user = user
        family.phone = request.POST['phone']
        family.save()

        camper = Camper()
        camper.family = family
        camper.first_name = user.first_name
        camper.last_name = user.last_name
        camper.under_18 = False
        camper.dob = None
        camper.save()

        return HttpResponseRedirect("/login/")

    return render(request, 'seabeck_draft/register.html', {})


def logout_view(request):
    logout(request)
    return redirect("/logout_successful/")


@login_required(login_url='/login_needed/')
def index(request):
    families_list = Family.objects.order_by("user__last_name")
#often use two underscores to represent dot/fk relationship
    template = loader.get_template('seabeck_draft/index.html')
    context = RequestContext(request, {'families_list': families_list})

    return HttpResponse(template.render(context))

@login_required()
def detail(request):

    family = get_object_or_404(Family, user=request.user)
    return render(request, 'seabeck_draft/detail.html', {'family': family})

@login_required()
def dynamic_detail(request, family_id):
    # family = get_object_or_404(Family, pk=family_id)
    return render(request, 'seabeck_draft/dynamic_detail.html', {})


def api_campers(request):

    years = EventYear.objects.all()
    current_year = list(reversed(years))[0]
    campers = Camper.objects.filter(family__user=request.user)
    output = []
    print(current_year)
    for camper in campers:
        in_current_year = len(Attendance.objects.filter(camper=camper, event_year=current_year)) > 0


        output.append({"id":camper.id, "name": camper.first_name + " " + camper.last_name,  "in_current_year" : in_current_year})


    return HttpResponse(json.dumps(output, indent=4), content_type="application/json")


# def api_detail(request, family_id):
#         family = get_object_or_404(Family, pk=family_id)
#     return render(request, 'seabeck_draft/detail.html', {'family': family})
#


def login_needed(request):
    return render(request, 'seabeck_draft/login_needed.html')

def logout_successful(request):
    return render(request, 'seabeck_draft/logout_successful.html')

def edit_family(request, family_id):

    if family_id == 0:
        print "new"
        family = Family()
    else:
        print "existing"
        family = get_object_or_404(Family, pk=family_id)

    filtered_family_list = Family.objects.filter(id=family_id)

#    if len(filtered_family_list) > 0:
    family = filtered_family_list[0]
#    else:
#        family = Family()

    if request.POST:
        print(request.POST)
        family.first_name = request.POST["first_name"]
        family.last_name = request.POST["last_name"]
        family.email = request.POST["email"]
        family.phone = request.POST["phone"]
        family.save()
        return HttpResponseRedirect("/")

    return render(request, 'seabeck_draft/edit_family.html', {'family': family})


def new_family(request):

    family = Family()

    if request.POST:
        print(request.POST)
        family.first_name = request.POST["first_name"]
        family.user.last_name = request.POST["user.last_name"]
        family.email = request.POST["email"]
        family.phone = request.POST["phone"]
        family.save()
        return HttpResponseRedirect("/")

    return render(request, 'seabeck_draft/new_family.html', {'family': family})


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
