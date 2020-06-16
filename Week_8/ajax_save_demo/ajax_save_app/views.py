from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Item
import json


def index(request):
    return render(request, "index.html", {})


@csrf_exempt
def api_model(request):
    if request.POST:
        print(request.POST)
        item = Item()
        item.name = request.POST["name"]
        item.save()
        item_json = json.dumps({
            "id": item.id,
            "name": item.name
        })
        return HttpResponse(item_json, content_type="application/json")
    item_list = Item.objects.order_by("-id")

    item_list_simple = []

    for item in item_list:
        item_list_simple.append({
            "id": item.id,
            "name": item.name
        })
    all_data = {
        "items": item_list_simple
    }
    json_response = json.dumps(all_data)

    return HttpResponse(json_response, content_type="application/json")
