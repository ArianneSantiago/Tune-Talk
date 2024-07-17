from django.shortcuts import get_object_or_404
from .models import Album, Rating

def rate_album_helper(album_id, user, rating_value):
    """
    Helper function to rate an album.
    
    Args:
        album_id (int): Primary key of the album to rate.
        user (User): The user who is rating the album.
        rating_value (int): The rating to assign to the album.
    
    Returns:
        None
    """

    album = get_object_or_404(Album, id=album_id)
    Rating.objects.filter(album=album, user=user).delete()
    album.ratings.create(user=user, rating=rating_value)