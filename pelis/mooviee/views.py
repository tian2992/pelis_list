from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Movie



class SingleMovie(DetailView):
    pass

class AllMovies(ListView):
    '''Todas las peli'''
    model = Movie
    template_name = 'mooviee/movie_list.html'


class ModernMovies(ListView):
    '''Peliculas mas recientes que 2000'''

    ### esto nos darias todas las pelis
    # queryset = Movie.objects.all()

    ## esto da todos los movie con Greaterh Than or Equal 2000
    queryset = Movie.objects.filter(year__gte=2000)
    template_name = 'mooviee/movie_list.html'


class DumbMovieSearch(View):
    base_query = Movie.objects

    def do_filter(self, arg):
        return DumbMovieSearch.base_query.filter(title__contains=arg)

    def get(self, request):
        return render(request, "mooviee/dumb_search.html")

    def post(self, request):
        moov = request.POST.get("movie_n")
        if moov == "":
            return 404
        # objects es un queryset buscando todos los valores de movie_n
        # objects = Movie.objects.filter(title__contains=moov)
        objects = self.do_filter(moov)
        return render(request, "mooviee/dumb_search.html", context=dict(object_list=objects))


##
#class AnimalAppointment():
#    created_time = datetime.now()
#    def check_available()
#
# class WebAppointment(AnimalAppointment, View):
#     def GET
#

#def dumb_movie_search(request):
#    post_data = request.POST
#    get_no = request.GET
#
#    render("dumb_search.html")