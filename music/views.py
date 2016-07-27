from django.views import generic
from .models import Album,Song
from .forms import AlbumForm,SongForm
from django.shortcuts import render
from django.shortcuts import redirect

class HomeView(generic.ListView):
    template_name='music/home.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.order_by('album_title')



class DetailView(generic.DetailView):
    model = Album
    context_object_name = 'a'
    template_name='music/album_detail.html'

def addAlbum(request):
    if request.method == "POST" :
        form = AlbumForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('music:home')
    else:
        form = AlbumForm()
    return render(request,'music/add_album.html',{'form':form})

def addSong(request,album_id):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.album = Album.objects.get(pk = album_id)
            obj.save()
            return redirect('music:album_detail',pk=album_id)
    else:
        form = SongForm()

    return render(request,'music/add_song.html',{'form':form})





