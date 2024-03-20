from django.contrib import admin
from .models import Album, Rating, Review

# Register your models here.

@admin.register(Album)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_year', 'status')
    list_filter = ('status', 'genre')
    date_hierarchy = 'created_on'

admin.site.register(Rating)

@admin.register(Review)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('content', 'album', 'user',)
    date_hierarchy = 'created_on'