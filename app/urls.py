from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('song-list/', views.song_list, name='song_list'),
    path('song/<str:song_id>/', views.display_song, name='display_song'),
    path('home/', views.home, name='home'),
    path('grid/', views.grid, name='grid'),
]