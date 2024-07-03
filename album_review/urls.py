from django.urls import path 
from . import views
"""
URL Configuration for Album Review App

This module defines the URL patterns for the Album Review app. It maps the URLs to the corresponding views.

URL Patterns:
- Home page URL: The root URL that displays the homepage.
- Detail page URL: URL pattern for displaying the details of a specific album.
- Review submission URL: URL pattern for submitting a review for a specific album.

"""
urlpatterns = [
    # path('', views.homepage, name='home'),
    # path('albums/', views.AlbumListView.as_view(), name='album_list'),
    # path('albums/add/', views.add_album, name='add_album'),
    # path('albums/<int:pk>/', views.album_detail, name='album_detail'),
    # path('albums/<int:pk>/rate/', views.rate_album, name='rate_album'),
    # path('albums/<int:pk>/edit_review/<int:review_id>/', views.review_edit, name='review_edit'),
    # path('albums/<int:pk>/delete_review/<int:review_id>/', views.review_delete, name='review_delete'),

    # Home page URL
    path('', views.home, name='home'),
    
    # Detail page URL
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    
    # Review submission URL
    path('album/<int:album_id>/review/', views.submit_review, name='submit_review'),
]

