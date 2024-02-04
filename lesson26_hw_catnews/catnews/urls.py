from django.urls import path, re_path
from .views import HomePageView, NewsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('news/<int:id>/', NewsPageView.as_view(), name='news_page',),


]