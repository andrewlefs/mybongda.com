from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    DetailView, ListView
)
from apps.relaxs.models import Relax
from apps.core.views import BaseView


# Create your views here.

class RelaxListView(BaseView, ListView):
    model = Relax
    context_object_name = 'list_object'
    template_name = 'relaxs/list.html'
    paginate_by = 10

    def get_queryset(self):
        return Relax.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Danh sách giải trí'
            },
        }
        context.update(info)
        return context


class RelaxDetailView(BaseView, DetailView):
    model = Relax
    template_name = 'relaxs/detail.html'

    @method_decorator(cache_page(10 * 60))
    def dispatch(self, request, *arg, **kwargs):
        return super().dispatch(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.name
            },
            'relaxs': Relax.objects.order_by('?')[0:8],
        }
        context.update(info)
        return context
