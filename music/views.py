from .models import Album,Song
from .forms import *
from django.shortcuts import render,redirect
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import View, UpdateView,CreateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

def HomeView(request):
    order_list = request.GET.get('order_by','album_title')
    if request.user.is_authenticated():
        albums = Album.objects.filter(user=request.user).order_by(order_list)
    else:
        albums = Album.objects.filter(user=14).order_by(order_list)
    context={'albums':albums}
    template_name = 'music/home.html'
    return render(request,template_name,context)

class AlbumDetailView(DetailView):
    model = Album
    context_object_name = 'a'
    template_name='music/album_detail.html'

class UpdateAlbum(LoginRequiredMixin,UpdateView):
    model = Album
    template_name='music/add_album.html'
    fields = ['album_title','artist','genre','album_logo']
    success_url = reverse_lazy('music:home')

class UpdateSong(LoginRequiredMixin,UpdateView):
    model = Song
    template_name='music/add_song.html'
    fields = ['song_title','audio_file','is_fav']

    def get_success_url(self):
        al = self.object.album
        return reverse_lazy('music:album_detail',args=(al.id,))

class UpdateUser(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UserForm
    template_name= 'music/change_profile.html'
    # fields = ['username','email','password']
    success_url = reverse_lazy('music:home')
    def get_object(self, queryset=None):
        return self.request.user

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

def logout_view(request):
    logout(request)
    return redirect('music:home')

class login_view(View):
    def get(self,request):
        return render(request,'music/login.html')
    def post(self,request):
        username = request.POST['u']
        password = request.POST['p']
        user = authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                # albums = Album.objects.filter(user=request.user)
                return redirect('music:home',)
            else:       #inactive user
                #using the messages framework
                messages.success(request,'Your account has been disabled')
                return redirect('music:home',)

        #form not valid- using the message framework
        messages.success(request,'Error. Please try again. Are you trying to create a new account?')
        return redirect('music:login',)


@login_required
def addAlbum(request):
        if request.method == "POST" :
            form = AlbumForm(request.POST,request.FILES)
            if form.is_valid():
                album = form.save(commit=False)
                album.user = request.user
                album.save()
                return redirect('music:home')
        else:
            form = AlbumForm()
        return render(request,'music/add_album.html',{'form':form})

@login_required
def addSong(request,album_id):
        if request.method == "POST":
            form = SongForm(request.POST,request.FILES)
            if form.is_valid():
                obj = form.save(commit = False)
                obj.album = Album.objects.get(pk = album_id)
                obj.save()
                return redirect('music:album_detail',pk=album_id)
        else:
            form = SongForm()

        return render(request,'music/add_song.html',{'form':form})

class DeleteAlbum(LoginRequiredMixin,DeleteView):
    model = Album
    template_name= 'music/delete.html'
    success_url = reverse_lazy('music:home')

class DeleteSong(LoginRequiredMixin,DeleteView):
    model = Song
    template_name= 'music/delete.html'
    success_url = reverse_lazy('music:home')

def SearchAlbum(request):
    query = request.GET.get('q','',)
    if(query):
        qset = (Q(album_title__startswith=query)|Q(album_title__endswith=query)|Q(album_title__icontains=query))
        results = Album.objects.filter(qset).distinct()
        if request.user.is_authenticated():
            results = results.filter(user=request.user).distinct()
    else:
        results = []
    if request.user.is_authenticated():
        albums = Album.objects.filter(user=request.user).order_by('album_title')
    else:
        albums = Album.objects.filter(user=1).order_by('album_title')
    c = {
        'albums':albums,
        'results':results,
        'query':query,
    }
    return render(request,'music/home.html',c)

@login_required
def Favorite_song(request,song_id):
        song = Song.objects.get(pk = song_id)
        song.is_fav = not song.is_fav
        song.save()
        al_id = song.album_id
        return redirect('music:album_detail',pk=al_id)

@login_required
def ViewFavoriteSongs(request):
        all_songs = Song.objects.all()
        fav_songs = [x for x in all_songs if x.getuser()==request.user and x.is_fav==True]
        template_name = 'music/fav_songs.html'
        return render(request,template_name,{'fav_songs':fav_songs})









