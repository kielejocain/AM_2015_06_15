from django.contrib import admin
from .models import Performer, Song, Playlist, PlaylistsSongs
# Register your models here.

admin.site.register(Performer)
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(PlaylistsSongs)
