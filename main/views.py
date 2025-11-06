from string import Template

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View, TemplateView

from goods.models import Category


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - главная'
        context['content'] =  'Магазин мебели HOME'
        return context

class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас'
        context['content'] = 'Текст о том, что наш магазин супер пупер'
        return context
# def index(request):
#
#     context = {
#         'title': 'Home',
#         'content': 'Магазин мебели Home',
#     }
#     return render(request, 'main/index.html', context)

# def about(request):
#     context = {
#         'title': 'Home - О нас',
#         'content': 'О нас',
#         'text_on_page': 'Текст о том, что наш магазин супер пупер'
#     }
#     return render(request, 'main/about.html', context)