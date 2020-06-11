from django.views.generic import ListView
from django.shortcuts import render
from django.db.models.query import QuerySet
from django.db.models.functions import Coalesce
from articles.models import Article, Theme, Theming


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles_query_set: QuerySet = Article.objects.all().order_by(ordering).prefetch_related('thems')
    dict_scopes = dict()

    for them in articles_query_set.order_by('id', '-theming__is_main', 'thems__name').values_list('id',  'thems__name',):
        current_them = dict_scopes.get(them[0])

        if current_them:
            current_them.append(them[1])
            #dict_scopes.update({them[0]: current_them})
        else:
            dict_scopes.update({them[0]: [them[1],]})

    # for key, value in dict_scopes.items():
    #     value.sort()
    #     dict_scopes.update({key: tuple(map(lambda theme: theme[1],value))})


    #print(dict_scopes)


    context = {'article_list': articles_query_set, 'thems_sort': dict_scopes}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by


    return render(request, template, context)
