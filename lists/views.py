from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    html = '<html>' \
           '<title>To-Do</title>' \
           '</html>'
    return HttpResponse(html)
