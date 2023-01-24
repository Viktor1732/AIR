from django import template

from airplanes.models import Category

register = template.Library()


@register.simple_tag(name='cats_tag')
def get_categories():
    return Category.objects.all()


@register.simple_tag(name='menu_tag')
def get_menu():
    menu = [{'title': 'О сайте', 'url_name': 'about'},
            {'title': 'Добавить статью', 'url_name': 'add_page'},
            {'title': 'Обратная связь', 'url_name': 'contact'},
            {'title': 'Войти', 'url_name': 'login'}]
    return menu
