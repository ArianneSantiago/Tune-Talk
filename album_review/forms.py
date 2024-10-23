from django import forms
from .models import Album, Review
from allauth.account.forms import SignupForm, LoginForm

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'release_year', 'genre', 'featured_image', 'status']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content',]

class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='Username')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.username = self.cleaned_data['username']
        user.save()
        return user

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].label = "Username or Email"