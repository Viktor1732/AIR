from django.http import HttpResponse


def index(request):
    return HttpResponse("HELLO!")


def categories(request):
    return HttpResponse("CATEGORIES_PAGE")