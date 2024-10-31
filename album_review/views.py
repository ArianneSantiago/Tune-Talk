from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Album, Rating, Review
from .forms import ReviewForm, AlbumForm, CustomLoginForm, CustomSignupForm
from .utils import rate_album_helper
from django.http import JsonResponse


class AlbumListView(ListView):
    """
    View class to display a list of albums.

     Attributes:
        template_name (str): The name of the template to use for rendering.
        queryset (QuerySet): The queryset of albums to display.
        context_object_name (str): The name of the context variable containing the queryset.
        paginate_by (int): The number of albums to display per page.
    """
    template_name = 'album_review/album_list.html'
    queryset = Album.objects.filter(status=1)
    context_object_name = 'album_list'
    paginate_by = 8

def homepage(request):
    """
    Render the homepage.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: Rendered homepage template.
    """
    user = request.user
    return render(request, 'album_review/homepage.html', {'user': user})

@login_required
def add_album(request):
    """
    Add a new album.

    POST requests: Save the form data and redirect to album detail page.
    GET requests: Render the form to add a new album.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: Rendered add_album template.
    """
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save()
            messages.success(request, 'Album added successfully.')
            return redirect('album_detail', pk=album.pk)
        else:
            messages.error(request, 'Error adding album.')
    else:
        form = AlbumForm()
    return render(request, 'album_review/add_album.html', {'form': form})

@login_required
def rate_album(request, pk):
    """
    Rate an album.

    POST requests: Save the rating for the album.
    Redirect to album detail page.

    Args:
        request: HttpRequest object.
        pk (int): Primary key of the album to rate.

    Returns:
        HttpResponseRedirect: Redirects to album detail page.
    """
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        rate_album_helper(pk, request.user, rating)
    return redirect('album_detail', pk=pk)

@login_required
def review_edit(request, pk, review_id):
    """
    Edit a review.

    POST requests: Save the edited review and redirect to album detail page.
    GET requests: Render the form to edit the review.

    Args:
        request: HttpRequest object.
        pk (int): Primary key of the album related to the review.
        review_id (int): Primary key of the review to edit.

    Returns:
        HttpResponse: Rendered review_edit template.
    """
    review = get_object_or_404(Review, pk=review_id)
    
    # Check if the current user is the owner of the review
    if review.user != request.user:
        messages.error(request, 'You do not have permission to edit this review.')
        return redirect('album_detail', pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated successfully.')
            return redirect('album_detail', pk=pk)
        else:
            messages.error(request, 'Error updating review.')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'album_review/review_edit.html', {'form': form})

@login_required
def review_delete(request, pk, review_id):
    """
    Delete a review.

    POST requests: Delete the review and redirect to album detail page.
    GET requests: No operation.

    Args:
        request: HttpRequest object.
        pk (int): Primary key of the album related to the review.
        review_id (int): Primary key of the review to delete.

    Returns:
        HttpResponseRedirect: Redirects to album detail page.
    """
    review = get_object_or_404(Review, pk=review_id)
    
    # Check if the current user is the owner of the review
    if review.user == request.user:
        review.delete()
        messages.success(request, 'Review deleted successfully.')
    else:
        messages.error(request, 'You are not allowed to delete this review.')
    
    return redirect('album_detail', pk=pk)

@login_required
def review_delete(request, pk, review_id):
    """
    Delete a review.

    POST requests: Delete the review and redirect to album detail page.
    GET requests: No operation.

    Args:
        request: HttpRequest object.
        pk (int): Primary key of the album related to the review.
        review_id (int): Primary key of the review to delete.

    Returns:
        HttpResponseRedirect: Redirects to album detail page.
    """
    review = get_object_or_404(Review, pk=review_id)
    if review.user == request.user:
        review.delete()
        messages.success(request, 'Review deleted successfully.')
    else:
        messages.error(request, 'You are not allowed to delete this review.')
    return redirect('album_detail', pk=pk)


def album_detail(request, pk):
    """
    Display details of an album.

    Fetches album details, associated reviews, and handles review submission.

    Args:
        request: HttpRequest object.
        pk (int): Primary key of the album to display.

    Returns:
        HttpResponse: Rendered album_detail template.
    """
    album = get_object_or_404(Album, id=pk, status=1)
    reviews = album.review_post.all().order_by("created_on")
    review_count = reviews.count()
    review_form = ReviewForm()

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.album = album
            review.save()
            messages.success(request, 'Review submitted')
            return redirect('album_detail', pk=pk)
        else:
            messages.error(request, 'Error submitting review.')

    return render(
        request, 
        "album_review/album_detail.html", 
        {"album": album, "reviews": reviews, "review_count": review_count, "review_form": review_form}
    )

@login_required
def rate_album(request, pk):
    """
    Rate an album.

    Allows a logged-in user to rate an album with a value between 1 and 5.

    Args:
        request: HttpRequest object.
        pk (int): Primary key of the album to rate.

    Returns:
        JsonResponse: JSON response indicating success or failure.
    """
    album = get_object_or_404(Album, pk=pk)
    rating = request.GET.get("rating")

    if rating and rating.isdigit():
        rating = int(rating)
        if 1 <= rating <= 5:
            rate_album_helper(album.id, request.user, rating)
            return JsonResponse({"success": True, "message": "Rating submitted!"})
        else:
            return JsonResponse({"success": False, "message": "Invalid rating value."})
    else:
        return JsonResponse({"success": False, "message": "Rating must be a number."})