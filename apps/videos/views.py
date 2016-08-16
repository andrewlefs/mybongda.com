from django.shortcuts import render
from django.views.generic import (
    DetailView, ListView
)
from apps.videos.models import Video
from apps.core.views import BaseView


# Create your views here.

class VideoListView(BaseView, ListView):
    model = Video
    context_object_name = 'list_object'
    template_name = 'videos/list.html'
    paginate_by = 15

    def get_queryset(self):
        return Video.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Highlight Video'
            },
        }
        context.update(info)
        return context


class VideoDetailView(BaseView, DetailView):
    model = Video
    template_name = 'videos/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.name
            },
            'videos_highlight': Video.objects.filter(category__name='Highlight').order_by('-id')[0:6],
        }
        context.update(info)
        return context
