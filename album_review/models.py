from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Album(models.Model):
    """
    Store a single album post
    """
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def average_rating(self) -> float:
        return Rating.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.title}: {self.average_rating()}"

    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField(default=0)

    def __str__(self):
         return f"{self.album.title}: {self.rating}"



    