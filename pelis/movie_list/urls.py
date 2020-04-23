from .views import MovieListView, MoveDetailView, MoveListDetailUserView
from django.urls import path

urlpatterns = [
    path("", MovieListView.as_view(), name= "movie-list"),
    path("moov/<int:pk>", MoveDetailView.as_view(), name="movie-detail"),
    path("mooser_list/<user_id>", MoveListDetailUserView.as_view(), name="movie-detail")

]
