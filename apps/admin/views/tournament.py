from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView
)
from django.conf import settings
from django.core.urlresolvers import reverse, reverse_lazy
from django import forms
from rest_framework import generics

from apps.core.views import AdminRequiredMixin, SuperUserRequiredMixin, AdminBaseView
from apps.tournaments.models import Tournament
from apps.tournaments.serializers import TournamentSerializer


class ListTournamentView(AdminBaseView, AdminRequiredMixin, ListView):
    template_name = 'admin/tournaments/list.html'
    model = Tournament
    paginate_by = settings.NUM_IN_PAGE

    def get_queryset(self):
        search = self.request.GET.get('q', None)
        if search:
            return Tournament.objects.filter(name__icontains=search).order_by('-id')
        else:
            return Tournament.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'List Tournament',
                'sidebar': ['tournament']
            }
        }
        search = self.request.GET.get('q', None)
        if search:
            info['q'] = search
        context.update(info)
        return context


class SearchTournamentByCountryView(generics.ListAPIView):
    serializer_class = TournamentSerializer

    def get_queryset(self):
        param = self.request.GET.get('q')
        return Tournament.objects.filter(country__id=param).order_by('-id')


class TournamentForm(forms.ModelForm):
    """docstring for TournamentForm"""

    class Meta:
        model = Tournament
        fields = ('name', 'slug', 'description',
                  'country', 'image')

        widgets = {
            'country': forms.widgets.Select(
                attrs={'class': 'form-control custom-select2',
                       'style': 'width: 100%;'})
        }


class CreateTournamentView(AdminBaseView, AdminRequiredMixin, CreateView):
    template_name = 'admin/tournaments/create.html'
    model = Tournament
    form_class = TournamentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Create Tournament',
                'sidebar': ['tournament']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_tournament')


class UpdateTournamentView(AdminBaseView, AdminRequiredMixin, UpdateView):
    template_name = 'admin/tournaments/update.html'
    model = Tournament
    form_class = TournamentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Update Tournament',
                'sidebar': ['tournament']
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:list_tournament')


class DeleteTournamentView(AdminBaseView, SuperUserRequiredMixin, DeleteView):
    model = Tournament

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:list_tournament')
