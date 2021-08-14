from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'maze/index.html')


def gameover(request):
    return render(request, 'maze/gameover.html')


def end(request):
    return render(request, "maze/end.html")


def two(request):
    return render(request, "maze/two.html")


def six(request):
    return render(request, "maze/six.html")


def seven(request):
    return render(request, "seven.html")
