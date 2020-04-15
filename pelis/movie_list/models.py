from django.db import models
from mooviee.models import Movie, Profile

# from django.contrib.auth.models import User


class MovieAssignment(models.Model):
    movie_list = models.ForeignKey("MovieList", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    seen = models.BooleanField(default=False)
    rating = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Movie: {self.movie} - User {self.user} - list {self.movie_list}"


class MovieList(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    movies = models.ManyToManyField(
        Movie,
        through='MovieAssignment',
        through_fields=('movie_list', 'movie', 'user'),
    )

# Create your models here.

