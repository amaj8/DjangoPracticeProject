from django.db import models

# Create your models here.
class Album(models.Model):
    album_title = models.CharField(max_length=1000)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + " by " + self.artist

class Song(models.Model):
    song_title = models.CharField(max_length=100)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title + " Album: "+ str(self.album)