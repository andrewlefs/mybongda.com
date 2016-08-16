from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
from apps.core.views import AdminRequiredMixin, SuperUserRequiredMixin, AdminBaseView
from apps.countries.models import Country


class ListCountryView(AdminBaseView, AdminRequiredMixin, ListView):
    template_name = 'admin/countries/list.html'
    model = Country
    paginate_by = settings.NUM_IN_PAGE

    def get_queryset(self):
        search = self.request.GET.get('q', None)
        if search:
            return Country.objects.filter(name__icontains=search).order_by('-id')
        else:
            return Country.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'List Country',
                'sidebar': ['country']
            }
        }
        search = self.request.GET.get('q', None)
        if search:
            info['q'] = search
        context.update(info)
        return context


class CreateCountryView(AdminBaseView, AdminRequiredMixin, CreateView):
    template_name = 'admin/countries/create.html'
    model = Country
    fields = ('name', 'slug', 'description',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Create Country',
                'sidebar': ['country']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_country')


class UpdateCountryView(AdminBaseView, AdminRequiredMixin, UpdateView):
    template_name = 'admin/countries/update.html'
    model = Country
    fields = ('name', 'slug', 'description',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Update Country',
                'sidebar': ['country']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_country')


class DeleteCountryView(AdminBaseView, SuperUserRequiredMixin, DeleteView):
    model = Country

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:list_country')
