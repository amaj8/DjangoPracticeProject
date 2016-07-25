from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
#from django.template import loader
from .models import Album,Song

# Create your views here.
def home(request):
    #text = "<h1>Welcome to the Music app homepage. Click on the links below to see more details</h1><br>"
    albums = Album.objects.all()
    #link = ''
    #for al in albums:
        #url = '/music/' + str(al.id) + '/'
        #url = str(al.id) + '/'
        #link += '<a href="' + url + '">' + al.album_title + '</a><br>'
    context = {
        "albums":albums,
    }
    #template = loader.get_template('music/home.html')

    return render(request,'music/home.html',context)




def latest(request):
    text = "<h1>This page displays the latest music added to the website"
    return HttpResponse(text)

def index(request):
    text = "<h1>Welcome to index page of the latest section</h1>"
    return HttpResponse(text)

def latest_num(request,number):
    song_num = int(number) + 4
    text= "<h2>Displaying latest song number %s"%(str(song_num) )
    return HttpResponse(text)

def about(request):
    text = "<h1>About page</h1>"
    return HttpResponse

def album_detail(request,album_id):
    a = get_object_or_404(Album,pk=album_id)
    """try:
        a = Album.objects.get(id=int(album_id))

    except Album.DoesNotExist:
        error_msg = "Error: That album id does not exist"
        raise Http404(error_msg)
    """
    context = {"a":a}
    return render(request,'music/form.html',context)

def form(request,album_id):
    a = get_object_or_404(Album,pk=album_id)
    selected_songs =[]              #empty list for all selected songs
    try:
        for key in request.POST.getlist('song'):
            song = a.song_set.get( pk = key )
            selected_songs.append(song)
    except (KeyError):
        error_msg = "You did not select any song"
        return render(request,'music/form.html',{'error_msg':error_msg})
    except (Song.DoesNotExist):
        error_msg = "The song does not exist"
        return render(request,'music/form.html',{'error_msg':error_msg})
    else:
        for song in selected_songs:
            song.is_fav = True
            song.save()
        return render(request,'music/form.html',{'a':a})

def defav(request,album_id):
    a = get_object_or_404(Album,pk=album_id)
    selected_songs = []
    try:
        for key in request.POST.getlist('song'):
            song = a.song_set.get(pk=key)
            selected_songs.append(song)
    except (KeyError):
        error_msg = "You did not select any song"
        return render(request,'music/form.html',{'error_msg':error_msg})
    except (Song.DoesNotExist):
        error_msg="The song does not exist"
        return render(request,'music/form.html',{'error_msg':error_msg})
    else:
        for song in selected_songs:
            song.is_fav=False
            song.save()
        return render(request,'music/form.html',{'a':a})


