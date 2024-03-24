from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Album, Rating, Review
from .views import *

class ViewsTestViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.album = Album.objects.create(title='Test Album', release_year=2022)

    def test_album_list_view(self):
        request = self.factory.get(reverse('album_list'))
        response = AlbumListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_homepage_view(self):
        request = self.factory.get(reverse('homepage'))
        request.user = self.user
        response = homepage(request)
        self.assertEqual(response.status_code, 200)

    def test_add_album_view(self):
        request = self.factory.get(reverse('add_album'))
        request.user = self.user
        response = add_album(request)
        self.assertEqual(response.status_code, 200)

    def test_rate_album_view(self):
        album = Album.objects.create(title='Test Album')
        request = self.factory.post(reverse('rate_album', kwargs={'pk': album.pk}), data={'rating': 5})
        request.user = self.user
        response = rate_album(request, album.pk)
        self.assertEqual(response.status_code, 302)

    def test_review_edit_view(self):
        album = Album.objects.create(title='Test Album')
        review = Review.objects.create(album=album, user=self.user, content='Test Review')
        request = self.factory.get(reverse('review_edit', kwargs={'pk': album.pk, 'review_id': review.pk}))
        request.user = self.user
        response = review_edit(request, album.pk, review.pk)
        self.assertEqual(response.status_code, 200)

    def test_review_delete_view(self):
        album = Album.objects.create(title='Test Album')
        review = Review.objects.create(album=album, user=self.user, content='Test Review')
        request = self.factory.post(reverse('review_delete', kwargs={'pk': album.pk, 'review_id': review.pk}))
        request.user = self.user
        response = review_delete(request, album.pk, review.pk)
        self.assertEqual(response.status_code, 302)

    def test_album_detail_view(self):
        album = Album.objects.create(title='Test Album')
        request = self.factory.get(reverse('album_detail', kwargs={'pk': album.pk}))
        response = self.client.get(reverse('album_detail', args=[self.album.pk]))
        self.assertEqual(response.status_code, 200)

    def test_rate_view(self):
        album = Album.objects.create(title='Test Album')
        request = self.factory.get(reverse('rate', kwargs={'album_id': album.pk, 'rating': 5}))
        request.user = self.user
        response = rate(request, album.pk, 5)
        self.assertEqual(response.status_code, 302)