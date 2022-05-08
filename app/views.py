from django.shortcuts import render, redirect
from .models import song
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    paginator = Paginator(song.objects.all(), 1)
    page_number = request.GET.get('page')
    #print('page_number', page_number)
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, "index.html", context)
 

def song_list(request):
    songs = song.objects.all()
    context = {'songs':songs}
    return render(request, 'song_list.html', context)

def display_song(request, song_id):
    page_obj = song.objects.filter(song_id=song_id).get()
    context = {'page_obj':page_obj}
    return render(request, 'songs.html' ,context)

def home(request):
    songs = song.objects.all()
    context = {'songs': songs}
    return render(request, 'home.html', context)

def grid(request):
    return render(request, 'grid.html')

