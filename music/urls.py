from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

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
    #url(r'^$',views.HomeView.as_view(),name='home'),
    url(r'^$',views.HomeView,name='home'),
    url(r'^(?P<pk>\d+)/$',views.DetailView.as_view(),name='album_detail'),
    url(r'^add/album/$',views.addAlbum,name='add_album'),
    url(r'^add/song/(?P<album_id>\d+)/$',views.addSong,name='add_song'),
    url(r'^update/album/(?P<album_id>\d+)/$',views.UpdateAlbum.as_view(),name='update_album'),
    url(r'^update/song/(?P<pk>\d+)/$',views.UpdateSong.as_view(),name='update_song'),
    url(r'^search/$',views.SearchAlbum,name='search_album'),
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^login/$',views.login_view.as_view(),name='login'),
]


if settings.DEBUG is True:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
