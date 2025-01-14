"""
Admin configuration for the movies app.
This module defines custom admin classes for the Genre and Movie models 
to customize their appearance and behavior in the Django admin interface.
"""

from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    """Configures the Genre model in the admin with specific list displays."""
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    """Configures the Movie model in the admin with excluded fields."""
    exclude = ('date_created',)

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
 
 
class MovieAdmin(admin.ModelAdmin):
    """Configures the Movie model in the admin with excluded fields."""
    exclude = ('date_created',)
