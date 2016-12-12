from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Album(models.Model):
    album_title = models.CharField(max_length=1000)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.ImageField()
    user = models.ForeignKey(User,default=1)     #1 = admin user


    def __str__(self):
        return self.album_title + " by " + self.artist

class Song(models.Model):
    song_title = models.CharField(max_length=100)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    is_fav = models.BooleanField(default=False)
    audio_file = models.FileField()

    def __str__(self):
        return self.song_title + " Album: "+ str(self.album)