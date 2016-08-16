from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    TemplateView, DetailView
)
from apps.pages.models import Page
from apps.core.views import BaseView


# Create your views here.

class PageDetailView(BaseView, DetailView):
    model = Page
    template_name = 'pages/detail.html'

    @method_decorator(cache_page(10 * 60))
    def dispatch(self, request, *arg, **kwargs):
        return super().dispatch(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.name
            },
        }
        context.update(info)
        return context
