from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    DetailView, ListView
)
from apps.clips.models import Clip
from apps.core.views import BaseView


# Create your views here.

class ClipListView(BaseView, ListView):
    model = Clip
    context_object_name = 'list_object'
    template_name = 'clips/list.html'
    paginate_by = 10

    def get_queryset(self):
        return Clip.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Tổng hợp bàn thắng'
            },
        }
        context.update(info)
        return context


class ClipDetailView(BaseView, DetailView):
    model = Clip
    template_name = 'clips/detail.html'

    @method_decorator(cache_page(10 * 60))
    def dispatch(self, request, *arg, **kwargs):
        return super().dispatch(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.name
            },
            'clips_highlight': Clip.objects.order_by('-id')[0:8],
        }
        context.update(info)
        return context
