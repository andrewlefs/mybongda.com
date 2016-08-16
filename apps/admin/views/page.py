from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView
)
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django import forms
from apps.core.views import AdminRequiredMixin, AdminBaseView
from apps.pages.models import Page


class ListPageView(AdminBaseView, AdminRequiredMixin, ListView):
    template_name = 'admin/pages/list.html'
    model = Page
    paginate_by = settings.NUM_IN_PAGE

    def get_queryset(self):
        return Page.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'List Page',
                'sidebar': ['page']
            }
        }
        context.update(info)
        return context


class PageForm(forms.ModelForm):
    """docstring for PageForm"""

    class Meta:
        model = Page
        fields = ('name', 'slug', 'content')


class CreatePageView(AdminBaseView, AdminRequiredMixin, CreateView):
    template_name = 'admin/pages/create.html'
    model = Page
    form_class = PageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Create Page',
                'sidebar': ['page']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_page')


class UpdatePageView(AdminBaseView, AdminRequiredMixin, UpdateView):
    template_name = 'admin/pages/update.html'
    model = Page
    form_class = PageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Update Page',
                'sidebar': ['page']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_page')


class DeletePageView(AdminBaseView, AdminRequiredMixin, DeleteView):
    model = Page

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:list_page')
