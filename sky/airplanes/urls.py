from django.urls import path

from .views import *

urlpatterns = [
    path('', AirplaneHome.as_view(), name='home'),
    path('about/', ShowAbout.as_view(), name='about'),
    path('add_page/', AddPost.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', AirplaneCategory.as_view(), name='category')
]
