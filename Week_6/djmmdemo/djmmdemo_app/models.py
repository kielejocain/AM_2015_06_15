from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Performer(models.Model):
    user = models.ForeignKey(User)
    stage_name = models.CharField(max_length=255)


class Playlist(models.Model):
    owner = models.ForeignKey(Performer)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=255)
    lyrics = models.TextField()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class PlaylistsSongs(models.Model):
    playlist = models.ForeignKey(Playlist)
    song = models.ForeignKey(Song)

    def __str__(self):
        return self.playlist.name + "-" + self.song.title

    def __unicode__(self):
        return self.playlist.name + "-" + self.song.title
