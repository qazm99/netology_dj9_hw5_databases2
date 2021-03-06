from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    ordering = '-published_at'
    qs = Article.objects.all().select_related('author', 'genre').defer('id', 'author__phone', 'published_at').order_by(ordering)
    context = {'object_list': qs}

    return render(request, template_name, context)
