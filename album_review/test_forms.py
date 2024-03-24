from django.test import TestCase
from .forms import AlbumForm, ReviewForm


class TestAlbumForm(TestCase):

    def test_album_form_valid_data(self):
        form = AlbumForm(data={
            'title': 'Test Album',
            'artist': 'Test Artist',
            'release_year': 2022,
            'genre': 'Test Genre',
            'status': 1
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_album_form_invalid_data(self):
        form = AlbumForm(data={})
        self.assertFalse(form.is_valid(), msg="Form is valid")


class TestReviewForm(TestCase):

    def test_review_form_valid_data(self):
        form = ReviewForm(data={
            'content': 'Test review content',
        })
        self.assertTrue(form.is_valid(), msg='Form is not valid')

    def test_review_form_invalid_data(self):
        form = ReviewForm(data={})
        self.assertFalse(form.is_valid(), msg="Form is valid")

