from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Album
# Create your views here.

class AlbumListView(ListView):
    """
    View class to display a list of albums.
    """
    template_name = 'album_review/album_list.html'
    queryset = Album.objects.filter(status=1)
    context_object_name = 'album_list'

class AlbumDetailView(DetailView):
    """
    View class to display details of a single album.
    """
    model = Album
    template_name = 'album_detail.html'
    context_object_name = 'album'