from django import forms
from .models import Album, Review

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'release_year', 'genre', 'featured_image', 'status']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content',]