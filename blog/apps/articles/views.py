# coding:utf-8

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article
from django.urls import reverse


def index(request):
    latest_articles_list = Article.objects.order_by('date_publ')[:3]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена!")
    latest_comm = a.comment_set.order_by('-id')[:10]
    return render(request, 'articles/detail.html', {'article':a,'latest_comm':latest_comm})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена!")
    a.comment_set.create(name_publ = request.POST['name'], text = request.POST['text'])
    
    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)))
