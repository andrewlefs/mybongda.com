from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView
)
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django import forms
from apps.core.views import AdminRequiredMixin, AdminBaseView
from apps.relaxs.models import Relax
from apps.categories.models import Category


class ListRelaxView(AdminBaseView, AdminRequiredMixin, ListView):
    template_name = 'admin/relaxs/list.html'
    model = Relax
    paginate_by = settings.NUM_IN_PAGE

    def get_queryset(self):
        return Relax.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(ListRelaxView, self).get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'List Relax',
                'sidebar': ['relax']
            }
        }
        context.update(info)
        return context


class RelaxForm(forms.ModelForm):
    """docstring for RelaxForm"""
    category = forms.ModelChoiceField(queryset=Category.objects.filter(type=2).order_by('-id'),
                                      widget=forms.Select(attrs={'class': 'form-control select2',
                                                                 'style': 'width: 100%;'}))

    class Meta:
        model = Relax
        fields = ('name', 'slug', 'description',
                  'image', 'frame', 'category')


class CreateRelaxView(AdminBaseView, AdminRequiredMixin, CreateView):
    template_name = 'admin/relaxs/create.html'
    model = Relax
    # initial = {
    #     'category': '1',
    # }
    form_class = RelaxForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Create Relax',
                'sidebar': ['relax']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_relax')


class UpdateRelaxView(AdminBaseView, AdminRequiredMixin, UpdateView):
    template_name = 'admin/relaxs/update.html'
    model = Relax
    form_class = RelaxForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Update Relax',
                'sidebar': ['relax']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_relax')


class DeleteRelaxView(AdminBaseView, AdminRequiredMixin, DeleteView):
    model = Relax

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:list_relax')
