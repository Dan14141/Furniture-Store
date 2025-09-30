from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'content': 'This is the content',
        'list': [1, 2, 3],
        'dict': {'First' : 1},
        'bool': True,
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("Hello, world. You're at about page.")