from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Album(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    description = models.TextField(null=True)
    #released = models.DateTimeField()

class Song(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    album_id = models.ForeignKey(Album, related_name='songs', on_delete = models.CASCADE)


    def __str__(self):
        return '%s' % (self.title)