from django.shortcuts import render
from django.http import HttpResponse

from .models import Dancer

def index(request):
    return HttpResponse("This is a dancer profile.")