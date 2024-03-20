from django.urls import path 

from . import views

urlpatterns = [
    path('', views.AlbumListView.as_view(), name='home'),
    path('albums/', views.AlbumListView.as_view(), name='album_list'),
    path('albums/<int:pk>/', views.album_detail, name='album_detail'),
    path('reviews/int:pk>/', views.album_detail, name='review_detail')
]
