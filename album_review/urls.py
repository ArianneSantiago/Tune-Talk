from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    AlbumListView, homepage, add_album, rate_album, review_edit,
    review_delete, album_detail, rate
)

urlpatterns = [
    path('', homepage, name='homepage'),
    path('add_album/', add_album, name='add_album'),
    path('album/<int:pk>/', album_detail, name='album_detail'),
    path('album/<int:pk>/rate/', rate_album, name='rate_album'),
    path('album/<int:pk>/review/<int:review_id>/edit/', review_edit, name='review_edit'),
    path('album/<int:pk>/review/<int:review_id>/delete/', review_delete, name='review_delete'),
    path('rate/<int:album_id>/<int:rating>/', rate, name='rate'),
    path('albums/', AlbumListView.as_view(), name='album_list'),  # Add this line
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)