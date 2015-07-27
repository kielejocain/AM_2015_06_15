from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.core.urlresolvers import reverse

from django.shortcuts import get_object_or_404, render

from .models import Registrant, Camper, Rate

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    registrants_list = Registrant.objects.order_by("-last_name")[:]

    template = loader.get_template('seabeck_draft/index.html')
    context = RequestContext(request, {'registrants_list': registrants_list})

    return HttpResponse(template.render(context))


def detail(request, registrant_id):
    registrant = get_object_or_404(Registrant, pk=registrant_id)
    return render(request, 'seabeck_draft/detail.html', {'registrant': registrant})


def edit_registrant(request, registrant_id):

    registrant = get_object_or_404(Registrant, pk=registrant_id)

    filtered_registrant_list = Registrant.objects.filter(id=registrant_id)

    if len(filtered_registrant_list) > 0:
        registrant = filtered_registrant_list[0]
    else:
        registrant = Registrant()

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
        registrant.last_name = request.POST["last_name"]
        registrant.email = request.POST["email"]
        registrant.phone = request.POST["phone"]
        registrant.save()
        return HttpResponseRedirect("/")

    return render(request, 'seabeck_draft/new_registrant.html', {'registrant': registrant})


def edit_camper(request, camper_id):

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
