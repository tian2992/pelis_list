from django.shortcuts import render

from django import forms



# Create your views here.
from django.views.generic import ListView, DetailView

from mooviee.models import Movie
#
# class MovieForm(forms.Form):
#     add_movie_pk = forms.IntegerField()
#     add_user_pk = forms.ImageField()


class MoveDetailView(DetailView):
    model = Movie


class MovieListView(ListView):
    model = Movie
    ## generates a context variable
    ## movie_list


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(MovieListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

    def get_queryset(self):
        ## result of movie_list
        return Movie.objects.filter()[:10]
        #       return Movie.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war


def my_movie_view(request):

    return render("my_movie.html")

def my_movie_add(request):

    pass


class ArticleForm(forms.Form):
    pass


def manage_articles(request):
    ArticleFormSet = formset_factory(ArticleForm)
    if request.method == 'POST':
        formset = ArticleFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            pass
    else:
        formset = ArticleFormSet()
    return render(request, 'manage_articles.html', {'formset': formset})