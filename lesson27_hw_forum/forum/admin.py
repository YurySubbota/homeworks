from django.contrib import admin
from forum.models import Room, Comment


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('picture', 'title', 'description', 'created_at', 'popularity')
    list_filter = ('title', 'created_at', 'popularity')
    search_fields = ('title', 'description')
    ordering = ('-created_at', 'title')
