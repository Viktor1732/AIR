from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import Airplane

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    posts = Airplane.objects.all()
    return render(request, 'airplanes/index.html', {'menu': menu, 'posts': posts, 'title': 'Авиация мира'})


def about(request):
    return render(request, 'airplanes/about.html', {'title': 'О сайте'})


def categories(request, catid):
    return HttpResponse(f"PAGE_WITH_CATEGORY_{catid}")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
