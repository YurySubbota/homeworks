from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views import View
from catnews.models import News, Comment


# Create your views here.

class HomePageView(View):
    TITLE = "Home Page"
    DEFAULT_NEWS_PICTURE = 'media/default.jpg'

    def get(self, request, *args, **kwargs):
        sort_by = request.GET.get('sort', 'pub_date')
        order_by = request.GET.get('order', 'desc')
        sort_by = sort_by if order_by == 'asc' else f'-{sort_by}'
        news = News.objects.order_by(sort_by)[:20]
        for new in news:
            desc_worlds_list = new.body.split(' ')[:10]
            description = ' '.join(desc_worlds_list)
            new.body = description

        return render(request, 'index.html',
                      context={'sort': sort_by, 'news_list': news, 'title': self.TITLE,
                               'default_jpg': self.DEFAULT_NEWS_PICTURE})


class NewsPageView(View):
    DEFAULT_NEWS_PICTURE = 'media/default.jpg'

    def get(self, request, id, *args, **kwargs):
        news = News.objects.get(pk=id)
        self.TITLE = news.title

        return render(request, 'news_page.html', context={'news': news, 'title': self.TITLE,
                                                          'default_jpg': self.DEFAULT_NEWS_PICTURE})
