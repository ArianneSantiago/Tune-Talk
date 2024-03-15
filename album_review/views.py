from django.shortcuts import render
# from django.http import HttpResponse
from .models import Album
# Create your views here.

def album_list(request):
    """
    View function to display a list of albums.
    """
    album = Album.objects.filter(status=1)
    context = {
        'album': album
    }
    return render(request, 'album_review/album_list.html', context)

def album_detail(request, album_id):
    """
    View function to display details of a single album.
    """
    album = Album.objects.get(id=album_id)
    context = {
        'album': album
    }
    return render(request, 'album_detail.html', context)