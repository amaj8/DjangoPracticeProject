from django.contrib import admin
from .models import Album,Song
# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    list_display=('album_title','artist','genre','album_logo','Songs')
    list_editable= ('artist',)
    def Songs(self,obj):
        return obj.song_set.all()

    Songs.empty_value_display = 'No Songs'

    ordering=('album_title',)
    search_fields=('album_title',)

class SongAdmin(admin.ModelAdmin):
    list_display = ('lower_case_song_title','is_fav','audio_file')
    list_display_links = None
    list_filter = ('is_fav',)


    def lower_case_song_title(self,obj):
        return ("%s" %(obj.song_title)).lower()
    lower_case_song_title.short_description = 'Title'
    empty_value_display = 'nil'

admin.site.register(Album,AlbumAdmin)

admin.site.register(Song,SongAdmin)