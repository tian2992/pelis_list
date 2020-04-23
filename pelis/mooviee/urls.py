from .views import AllMovies, ModernMovies

from django.urls import path


urlpatterns = [
    path("/", AllMovies.as_view(), name='all_movies' ),
    path('/modern-movie', ModernMovies.as_view(), name = "recent_movies")
]
