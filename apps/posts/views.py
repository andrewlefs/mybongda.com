from django.shortcuts import render
from django.views.generic import (
    TemplateView, DetailView, ListView
)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from apps.posts.models import Post
from apps.core.views import BaseView


# Create your views here.

class PostListView(BaseView, ListView):
    model = Post
    context_object_name = 'list_object'
    template_name = 'posts/list.html'
    paginate_by = 10

    def get_queryset(self):
        danh_muc = self.request.GET.get('danh-muc', None)
        if danh_muc:
            return Post.objects.filter(category__id=danh_muc).order_by('-id')
        return Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Danh sách tin tức'
            },
        }
        context.update(info)
        return context


class PostDetailView(BaseView, DetailView):
    model = Post
    template_name = 'posts/detail.html'

    @method_decorator(cache_page(10 * 60))
    def dispatch(self, request, *arg, **kwargs):
        return super().dispatch(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.name
            },
            'post_related': Post.objects.order_by('?')[0:6],
        }
        context.update(info)
        return context
