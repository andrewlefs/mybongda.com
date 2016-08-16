from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView)
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
from django import forms
from apps.core.views import AdminRequiredMixin, SuperUserRequiredMixin, AdminBaseView
from apps.channels.models import Channel


class ListChannelView(AdminBaseView, AdminRequiredMixin, ListView):
    template_name = 'admin/channels/list.html'
    model = Channel
    paginate_by = settings.NUM_IN_PAGE

    def get_queryset(self):
        search = self.request.GET.get('q', None)
        if search:
            return Channel.objects.filter(name__icontains=search).order_by('-id')
        else:
            return Channel.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'List Channel',
                'sidebar': ['channel']
            }
        }
        search = self.request.GET.get('q', None)
        if search:
            info['q'] = search
        context.update(info)
        return context


class ChannelForm(forms.ModelForm):
    """docstring for SubjectForm"""

    class Meta:
        model = Channel
        fields = ('name', 'slug', 'description',
                  'image', 'link', 'frame')


class CreateChannelView(AdminBaseView, AdminRequiredMixin, CreateView):
    template_name = 'admin/channels/create.html'
    model = Channel
    form_class = ChannelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Create Channel',
                'sidebar': ['channel']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_channel')


class UpdateChannelView(AdminBaseView, AdminRequiredMixin, UpdateView):
    template_name = 'admin/channels/update.html'
    model = Channel
    form_class = ChannelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Update Channel',
                'sidebar': ['channel']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_channel')


class DeleteChannelView(AdminBaseView, SuperUserRequiredMixin, DeleteView):
    model = Channel

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:list_channel')
