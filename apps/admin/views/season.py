from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView,
)
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
from apps.core.views import AdminRequiredMixin, SuperUserRequiredMixin, AdminBaseView
from apps.seasons.models import Season


class ListSeasonView(AdminBaseView, AdminRequiredMixin, ListView):
    template_name = 'admin/seasons/list.html'
    model = Season
    paginate_by = settings.NUM_IN_PAGE

    def get_queryset(self):
        return Season.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'List Season',
                'sidebar': ['season']
            }
        }
        context.update(info)
        return context


class CreateSeasonView(AdminBaseView, AdminRequiredMixin, CreateView):
    template_name = 'admin/seasons/create.html'
    model = Season
    fields = ('name', 'slug', 'description',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Create Season',
                'sidebar': ['season']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_season')


class UpdateSeasonView(AdminBaseView, AdminRequiredMixin, UpdateView):
    template_name = 'admin/seasons/update.html'
    model = Season
    fields = ('name', 'slug', 'description',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Update Season',
                'sidebar': ['season']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_season')


class DeleteSeasonView(AdminBaseView, SuperUserRequiredMixin, DeleteView):
    model = Season

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:list_season')
