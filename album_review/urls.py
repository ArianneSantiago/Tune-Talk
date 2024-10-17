from django.urls import path 
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('albums/', views.AlbumListView.as_view(), name='album_list'),
    path('albums/add/', views.add_album, name='add_album'),
    path('albums/<int:pk>/', views.album_detail, name='album_detail'),
    path('albums/<int:pk>/rate/', views.rate_album, name='rate_album'),
    path('albums/<int:pk>/edit_review/<int:review_id>/', views.review_edit, name='review_edit'),
    path('albums/<int:pk>/delete_review/<int:review_id>/', views.review_delete, name='review_delete'),

]

