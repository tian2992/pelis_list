from django.contrib import admin

# Register your models here.


from .models import MovieList, MovieAssignment

admin.site.register(MovieList)
admin.site.register(MovieAssignment)