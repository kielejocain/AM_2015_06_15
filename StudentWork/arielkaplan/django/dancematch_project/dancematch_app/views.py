from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from .models import Dancer, Dance, Schedule, Location, DancePrefs, SkillLevel, Goals, Activity, DanceRole

import json


def index(request):
    all_dancers = Dancer.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'all_dancers': all_dancers,
    })
    return HttpResponse(template.render(context))


def profile(request, dancer_id):
    # Kevin's preferred method: less reliant on builtin functions; two steps
    # filtered_dancer_list = Question.objects.filter(id=dancer_id)
    # dancer = filtered_dancer_list[0]
    dancer = get_object_or_404(Dancer, pk=dancer_id)
    # dance_prefs = get_list_or_404(DancePrefs, dancer=dancer)
    dance_prefs = DancePrefs.objects.filter(dancer=dancer)
    return render(request, 'profile.html', {'dancer': dancer,
                                            'dance_prefs': dance_prefs,
                                            })


def dances(request):
    all_dances = Dance.objects.all()
    template = loader.get_template('dances.html')
    context = RequestContext(request, {
        'all_dances': all_dances,
    })
    return HttpResponse(template.render(context))


def edit_profile(request, dancer_id):
    dancer = get_object_or_404(Dancer, pk=dancer_id)
    dance_prefs = DancePrefs.objects.filter(dancer=dancer)
    if request.POST:
        print(request.POST)
        dancer.name = request.POST["name"]
        dancer.email = request.POST["email"]
        dancer.bio = request.POST["bio"]
        dancer.active_member = request.POST.get("active_member", False)
        dancer.save()
    return render(request, 'edit.html', {'dancer': dancer,
                                         'dance_prefs': dance_prefs,
                                         })


def edit_dance(request, dancer_id, dance_pref_id):
    dancer = get_object_or_404(Dancer, pk=dancer_id)
    dance_pref = get_object_or_404(DancePrefs, id=dance_pref_id)
    dances = Dance.objects.all()
    roles = DanceRole.objects.all()
    activities = Activity.objects.all()
    goals = Goals.objects.all()
    skill_levels = SkillLevel.objects.all()
    if request.POST:
        print(request.POST)
        dance_pref.dance = request.POST.get("dance")
        dance_pref.role = request.POST.get("role")
        dance_pref.skill_level = request.POST.get("skill_level")
        dance_pref.activity = request.POST.get("activity")
        dance_pref.goal = request.POST.get("goal")
        dance_pref.save()
    return render(request, 'edit_dance.html', {'dancer': dancer,
                                               'dance_pref': dance_pref,
                                               'dances': dances,
                                               'roles': roles,
                                               'activities': activities,
                                               'goals': goals,
                                               'skill_levels': skill_levels,
                                               })
