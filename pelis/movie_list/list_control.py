from movie_list.models import Movie, Profile, MovieList, MovieAssignment
from django.contrib.auth.models import User


my1 = Movie(title="Spiderman", year=2002, country="us", director="Sam Raimi")
my1.save()
my2 = Movie(title="Spiderman 2", year=2004, country="us", director="Sam Raimi")
my2.save()
my3 = Movie(title="Spiderman 3", year=2007, country="us", director="Sam Raimi")
my3.save()

# from django.contrib.auth import get_user

u = User.objects.all().first()
p = u.profile

my_list = MovieList(title="Spuder", user=p)