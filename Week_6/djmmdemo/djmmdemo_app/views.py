from django.http import *
import json
from .models import *


def api_post(request, model_name):
    response_message = {}
    if "lists" == model_name:
        song_id = request.POST["song_id"]
        playlist_id = request.POST["playlist_id"]
        lists = PlaylistsSongs.objects.filter(song__id=song_id, playlist__id=playlist_id)
        if len(lists) == 0:
            print("EXISTING")
    return HttpResponse(json.dumps(response_message, indent=4), content_type="application/json")


def api_get(request):
    data = {"lists": {}, "all":[]}
    for s in Song.objects.all():
        data["all"].append({"title": s.title, "id": s.id})
    for p in Playlist.objects.all():
        playlist = {"name": p.name, "songs": []}
        for sp in PlaylistsSongs.objects.filter(playlist=p):
            playlist["songs"].append({"title": sp.song.title, "id": sp.song.id})
        data["lists"][p.id] = playlist
    return HttpResponse(json.dumps(data, indent=4), content_type="application/json")
