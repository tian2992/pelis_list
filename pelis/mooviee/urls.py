from .views import AllMovies

from django.urls import path


urlpatterns = [
    path("/", AllMovies.as_view(), name='all_movies' ),got
]
