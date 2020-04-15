from .views import MovieListView, MoveDetailView

from django.urls import path



urlpatterns = [

    path("", MovieListView.as_view(), name= "movie-list"),
    path("moov/<int:pk>", MoveDetailView.as_view(), name= "movie-detail")
    ]
