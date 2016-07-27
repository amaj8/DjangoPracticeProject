from django.conf.urls import url
from . import views

app_name = 'music'
"""
urlpatterns = [
    url(r'^$',views.home,name = 'home'),
    url(r'^latest/index/',views.index, name = 'index'),
    url(r'^latest/$',views.latest,name = 'latest'),
    url(r'^latest/(\d{1,2})',views.latest_num,name = 'latest_num'),
    #url(r'^about/./r',views.about,name ='about'),
    url(r'^(?P<album_id>\d+)/$',views.album_detail,name='album_detail'),
    url(r'^(?P<album_id>\d+)/favourite/$', views.form , name='favourite'),
    url(r'^(?P<album_id>\d+)/defavourite/$',views.defav, name='defavourite')
    #url(r'^(\d+)/$',views.album_detail,name='album_detail'),
]
"""

urlpatterns= [
    url(r'^$',views.HomeView.as_view(),name='home'),
    url(r'^(?P<pk>\d+)/$',views.DetailView.as_view(),name='album_detail'),
    url(r'^add/album/$',views.addAlbum,name='add_album'),
    url(r'^add/song/(?P<album_id>\d+)/$',views.addSong,name='add_song'),
]