from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Este Profile tiene una relacion uno uno con cada user model.

    Envelops user object into user field
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Profile-User: {self.user}"


class Movie(models.Model):

    title = models.CharField(max_length=100)
    year = models.IntegerField()

    country = models.CharField(max_length=2)
    synopsis = models.TextField(null=True)
    age_ranking = models.CharField(max_length=8)

    director = models.CharField(null=True, max_length=30)

    def __str__(self):
        return f"M: {self.title} ({self.year})"
    # Actors
    # Director