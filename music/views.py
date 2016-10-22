from django.views import generic
from django.views.generic import View
from .models import Album,Song
from .forms import *
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.contrib.auth import authenticate,login

from django.views.generic.edit import CreateView, UpdateView ,DeleteView

class HomeView(generic.ListView):
    template_name='music/home.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all().order_by('album_title')

class DetailView(generic.DetailView):
    model = Album
    context_object_name = 'a'
    template_name='music/album_detail.html'

class UpdateAlbum(generic.UpdateView):
    model = Album
    template_name='music/add_album.html'

class UpdateSong(UpdateView):
    model = Song
    template_name='music/add_song.html'
    fields = ['song_title']
    success_url = reverse_lazy('music:album_detail')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration.html'

    #display blank registration form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('music:home',)

        #if form is not valid or the user is not active then return a blank form
        return render(request,self.template_name,{'form':form,})

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

def DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy('music:home')

def SearchAlbum(request):
    query = request.GET.get('q','',)
    if(query):
        qset = (Q(album_title__startswith=query)|Q(album_title__endswith=query)|Q(album_title__icontains=query))
        results = Album.objects.filter(qset).distinct()
    else:
        results = []
    albums = Album.objects.all().order_by('album_title')
    c = {
        'albums':albums,
        'results':results,
        'query':query,
    }
    return render(request,'music/home.html',c)

def Home(request):
    albums = Album.objects.all()
    asc = request.GET.get('asc','',)

    if asc:
        albums.order_by('album_title')

    context= {
        'albums' : albums,
    }

    #if request.user.is_authenticated():
     #   context += {'user':request.user}
    return render(request,'music/home.html',context)




