from django.db import models
from django.urls import reverse


class Airplane(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    content = models.TextField(blank=True, verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', null=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Авиация'
        verbose_name_plural = 'Авиация'
        ordering = ['time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    login = models.CharField(max_length=50, null=True, verbose_name='Логин')
    email = models.EmailField(max_length=50, verbose_name='Email')
    message = models.TextField(max_length=500, verbose_name='Сообщение')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['name']
