from django.views.generic import (
    ListView, DeleteView
)
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.core.views import AdminRequiredMixin, AdminBaseView
from apps.clips.models import Clip
from apps.core import utils


class ListClipView(AdminBaseView, AdminRequiredMixin, ListView):
    template_name = 'admin/clips/list.html'
    model = Clip
    paginate_by = settings.NUM_IN_PAGE

    def get_queryset(self):
        return Clip.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'List Clip',
                'sidebar': ['clip']
            }
        }
        context.update(info)
        return context


class AutoGetClipView(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        utils.get_list_clip_ball()
        return Response(True)


class DeleteClipView(AdminBaseView, AdminRequiredMixin, DeleteView):
    model = Clip

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:list_clip')
