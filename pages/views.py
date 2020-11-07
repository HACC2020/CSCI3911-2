from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello, World!')
