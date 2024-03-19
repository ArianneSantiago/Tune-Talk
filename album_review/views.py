from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Album, Rating, Review
from  .forms import ReviewForm

# Create your views here.

class AlbumListView(ListView):
    """
    View class to display a list of albums.
    """
    template_name = 'album_review/album_list.html'
    queryset = Album.objects.filter(status=1)
    context_object_name = 'album_list'

# class AlbumDetailView(DetailView):
#     """
#     View class to display details of a single album.
#     """
#     model = Album
#     template_name = 'album_detail.html'
#     context_object_name = 'album'

def album_detail(request, album_id):

    album = get_object_or_404(Album, id=album_id, status=1)
    review = album.review_post.all().order_by("-created_on")
    review_count = album.review_post.count()

    if request.method == 'POST':

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.album = album
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted'
            )
    
    review_form = ReviewForm()

    return render(
        request, "album_review/album_detail.html", {
            "album": album,
            "review": review,
            "review_count": review_count,
            "review_form": review_form,
        },
    )

def review_edit(request, album_id, review_id):

    if request.method == "POST":

        album = get_object_or_404(Album, id=album_id, status=1)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.user == request.user:
            review = review_form.save(commit=False)
            review.album = album
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('album_detail', args=[album_id]))


def review_delete(request, album_id, review_id):

    album = get_object_or_404(Album, id=album_id, status=1)
    review = get_object_or_404(Review, pk=review_id)

    if review_user == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('album_detail', args=[album_id]))


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

# def review_list(request):
#     reviews = Review.objects.all()
#     return render(request, 'album_detail.html', {'reviews': reviews})

# def add_review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('album_detail.html')
#     else:
#         form = ReviewForm()
#     return render(request, 'album_detail.html', {'form': form})

# def edit_review(request, album_id):
#     review = get_object_or_404(Review, pk=album_id)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST, instance=review)
#         if form.is_valid():
#             form.save()
#             return redirect('album_detail.html')
#     else:
#         form = ReviewForm(instance=review)
#     return render(request, )
