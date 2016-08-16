from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView)
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
from django import forms
from apps.core.views import AdminRequiredMixin, SuperUserRequiredMixin, AdminBaseView
from apps.teams.models import Team


class ListTeamView(AdminBaseView, AdminRequiredMixin, ListView):
    template_name = 'admin/teams/list.html'
    model = Team
    paginate_by = settings.NUM_IN_PAGE

    def get_queryset(self):
        search = self.request.GET.get('q', None)
        if search:
            return Team.objects.filter(name__icontains=search).order_by('-id')
        else:
            return Team.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'List Team',
                'sidebar': ['team']
            }
        }
        search = self.request.GET.get('q', None)
        if search:
            info['q'] = search
        context.update(info)
        return context


class TeamForm(forms.ModelForm):
    """docstring for SubjectForm"""

    class Meta:
        model = Team
        fields = ('name', 'slug', 'description',
                  'image', 'country')

        widgets = {
            'country': forms.widgets.Select(
                attrs={'class': 'form-control select2',
                       'style': 'width: 100%;'}),
        }


class CreateTeamView(AdminBaseView, AdminRequiredMixin, CreateView):
    template_name = 'admin/teams/create.html'
    model = Team
    form_class = TeamForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Create Team',
                'sidebar': ['team']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_team')


class UpdateTeamView(AdminBaseView, AdminRequiredMixin, UpdateView):
    template_name = 'admin/teams/update.html'
    model = Team
    form_class = TeamForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Update Team',
                'sidebar': ['team']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_team')


class DeleteTeamView(AdminBaseView, SuperUserRequiredMixin, DeleteView):
    model = Team

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:list_team')
