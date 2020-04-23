from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from pelis.mooviee.models import Movie



class AllMovies(ListView):
    '''Todas las peli'''
    model = Movie


class ModernMovies(ListView):
    '''Peliculas mas recientes que 2000'''

    ### esto nos darias todas las pelis
    # queryset = Movie.objects.all()

    ## esto da todos los movie con Greaterh Than or Equal 2000
    queryset = Movie.objects.filter(year__gte=2000)

