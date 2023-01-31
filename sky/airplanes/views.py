from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .forms import AddAirplaneForm, RegisterUserForm, LoginUserForm, ContactForm
from .models import Airplane
from .utils import DataMixin


class AirplaneHome(DataMixin, ListView):
    model = Airplane
    template_name = 'airplanes/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Airplane.objects.filter(is_published=True)


class ShowAbout(DataMixin, TemplateView):
    template_name = 'airplanes/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Информация о сайте', cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))


class AddPost(DataMixin, CreateView):
    form_class = AddAirplaneForm
    template_name = 'airplanes/add_page.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи', cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))


class ContactCreate(DataMixin, CreateView):
    form_class = ContactForm
    template_name = 'airplanes/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обратная связь'
        c_def = self.get_user_context(cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = Airplane
    context_object_name = 'post'
    template_name = 'airplanes/show_post.html'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'], cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))


class AirplaneCategory(DataMixin, ListView):
    model = Airplane
    template_name = 'airplanes/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Airplane.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'airplanes/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация пользователя'
        c_def = self.get_user_context(cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'airplanes/login.html'
    success_url = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        c_def = self.get_user_context(cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
