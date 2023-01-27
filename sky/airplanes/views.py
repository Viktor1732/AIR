from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import AddAirplaneForm
from .models import Airplane


class AirplaneHome(ListView):
    model = Airplane
    template_name = 'airplanes/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Airplane.objects.filter(is_published=True)


def about(request):
    return render(request, 'airplanes/about.html', {'title': 'О сайте'})


def add_page(request):
    if request.method == 'POST':
        form = AddAirplaneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddAirplaneForm()
    return render(request, 'airplanes/add_page.html', {'form': form, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse('<h1>Обратная связь</1>')


def login(request):
    return HttpResponse("<h1>ВХОД</h1>")


def show_post(request, post_slug):
    posts = get_object_or_404(Airplane, slug=post_slug)
    context = {
        'title': posts.title,
        'post': posts
    }
    return render(request, 'airplanes/show_post.html', context=context)


def show_category(request, cat_id):
    posts = Airplane.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'title': 'Отображение по рубрикам',
        'post': posts,
        'cat_selected': cat_id
    }
    return render(request, 'airplanes/category.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
