from .views import AllMovies, ModernMovies, DumbMovieSearch
    # , dumb_movie_search

from django.urls import path


urlpatterns = [
    path("", AllMovies.as_view(), name='all_movies' ),
    path('modern-movie', ModernMovies.as_view(), name = "recent_movies"),
    path('dumb-search', DumbMovieSearch.as_view(), name="bad-movie-search")
]
