from django.contrib import admin
from catnews.models import News, Comment
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('picture', 'author',
                    'title', 'body', 'pub_date',
                    'rating', 'popularity')
    ordering = ('author',
                    'title', 'pub_date',
                    'rating', 'popularity')
    search_fields = ('author', 'title', )
