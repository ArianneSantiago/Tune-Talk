from django.urls import path 
# from .views import AlbumListView, AlbumDetailView
from . import views

urlpatterns = [
    path('albums/', views.AlbumListView.as_view(), name='album_list'),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
]
