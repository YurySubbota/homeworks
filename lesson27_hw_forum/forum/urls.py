from django.contrib import admin
from django.urls import path
from .views import RoomsListView, RoomView, NewCommentView, NewCommentForCommentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RoomsListView.as_view(), name='rooms_list'),
    path('room/<int:pk>/', RoomView.as_view(), name='room'),
    path('new_comment/<int:pk>/', NewCommentView.as_view(), name='new_comment'),
    path('new_comment_for_comment/<int:pk>/', NewCommentForCommentView.as_view(), name='new_comment_for_comment')
]
