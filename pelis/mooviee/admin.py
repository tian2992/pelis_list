from django.contrib import admin

# Register your models here.

from .models import Movie, Profile, User

admin.site.register(Movie)
admin.site.register(Profile)