from django import forms
from .models import Album,Song
from django.contrib.auth.models import User

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields =('album_title','artist','genre','album_logo',)
        labels= {
            'album_title' : 'Enter the title of the album',
            'artist' : 'Enter the name of the artist',
            'genre' : 'Enter the genre',
        }
        error_messages={
            'album_title':{
                'required': 'Sorry, albums without names aren\'t allowed',
            },
        }


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('song_title','audio_file','is_fav')
        labels={
            'song_title':'Enter the name of the song',
            'is_fav':'Mark it as my favourite',
            'audio_file':'Please upload the audio file',
        }

class AForm(forms.Form):
    album_title = forms.CharField(label="Enter the title of the album",max_length=100)
    artist = forms.CharField(label="Enter the name of the artist",max_length=100)
    genre = forms.CharField(label="Enter the genre",max_length=100)
    album_logo = forms.FileField(required=False)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password',]
