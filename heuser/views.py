from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'heuser/index.html')

def hls(request):
    return HttpResponse('Hallo Welt')
