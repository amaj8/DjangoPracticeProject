from django import forms
from .models import Album,Song

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields =('album_title','artist','genre','album_logo',)