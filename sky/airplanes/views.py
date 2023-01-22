from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import Airplane

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]


def index(request):
    posts = Airplane.objects.all()
    context = {
        'menu': menu,
        'posts': posts,
        'title': "Авиация мира"
    }
    return render(request, 'airplanes/index.html', context=context)


def about(request):
    return render(request, 'airplanes/about.html', {'title': 'О сайте'})


def add_page(request):
    return HttpResponse('<h1>Добавить страницу</h1>')


def contact(request):
    return HttpResponse('<h1>Обратная связь</1>')


def login(request):
    return HttpResponse("<h1>ВХОД</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
