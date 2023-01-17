from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("HELLO!")


def categories(request, catid):
    return HttpResponse(f"PAGE_WITH_CATEGORY_{catid}")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
