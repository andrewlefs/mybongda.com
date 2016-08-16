from django.shortcuts import render
from django.views.generic import (
    DetailView
)
from apps.channels.models import Channel
from apps.fixtures.models import Fixture
from django.http import HttpResponseServerError
from apps.core.views import BaseView
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator


# Create your views here.

class ChannelDetailView(BaseView, DetailView):
    model = Channel
    template_name = 'channels/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.name
            }
        }
        context.update(info)
        try:
            fixture = self.kwargs['fixture']
            if fixture:
                context['fixture'] = Fixture.objects.get(id=fixture)
            else:
                return HttpResponseServerError(content="500 error")
        except:
            return HttpResponseServerError(content="500 error")
        return context


class ChannelFrameDetailView(BaseView, DetailView):
    model = Channel
    template_name = 'channels/frame.html'

    @method_decorator(xframe_options_exempt)
    def dispatch(self, request, *arg, **kwargs):
        return super().dispatch(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.name
            }
        }
        context.update(info)
        return context
