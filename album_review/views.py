from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Album, Rating
# Create your views here.

class AlbumListView(ListView):
    """
    View class to display a list of albums.
    """
    # template_name = 'album_review/album_list.html'
    queryset = Album.objects.filter(status=1)
    context_object_name = 'album_list'

class AlbumDetailView(DetailView):
    """
    View class to display details of a single album.
    """
    model = Album
    template_name = 'album_detail.html'
    context_object_name = 'album'


def index(request: HttpRequest) -> HttpResponse:
    albums = Album.objects.all()
    for album in albums:
        rating = Rating.objects.filter(album=album, user=request.user).first()
        album.user_rating = rating.rating if rating else 0
    return render(request, "album_detail.html", {"albums": albums})


def rate(request: HttpRequest, album_id: int, rating:int) -> HttpResponse:
    """
    This views checks if the user has made any rating for each album, and, if so,
    saves it into the list so we can display it at the Front-End
    """
    albums = Album.objects.get(id=album_id)
    Rating.objects.filter(album=album, user=request.user).delete()
    album.rating_set.create(user=request.user, rating=rating)
    return index(request)
