from django.views import generic
from .models import Album,Song
from .forms import AlbumForm
from django.shortcuts import render
from django.shortcuts import redirect

class HomeView(generic.ListView):
    template_name='music/home.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    context_object_name = 'a'
    template_name='music/album_detail.html'

def addNew(request):
    if request.method == "POST" :
        form = AlbumForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('music:home')
    else:
        form = AlbumForm()
    return render(request,'music/add_album.html',{'form':form})




