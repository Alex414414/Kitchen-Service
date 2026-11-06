from django.http import HttpResponse
from django.views import View


def index(request):
    return HttpResponse("Kitchen Service")
