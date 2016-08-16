from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView, FormView
)
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django import forms
from django.conf import settings
from datetime import datetime, timedelta
from rest_framework import generics
from apps.core.views import AdminRequiredMixin, AdminBaseView
from apps.teams.models import Team
from apps.teams.serializers import TeamSerializer
from apps.fixtures.models import Fixture
from apps.matches.models import Match
from apps.tournaments.models import Tournament


class ListFixtureView(AdminBaseView, AdminRequiredMixin, ListView):
    template_name = 'admin/fixtures/list.html'
    model = Fixture
    paginate_by = settings.NUM_IN_PAGE

    def get_queryset(self):
        now = datetime.now() - timedelta(hours=2)
        return Fixture.objects.filter(start_date__gte=now).order_by('start_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'List Fixture',
                'sidebar': ['fixture']
            }
        }
        context.update(info)
        return context


class SearchFixtureView(generics.ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        param = self.request.GET.get('q')
        return Team.objects.filter(name__icontains=param).order_by('-name')


class FixtureForm(forms.ModelForm):
    """docstring for SubjectForm"""
    team_home = forms.IntegerField()
    team_away = forms.IntegerField()
    tournament = forms.IntegerField()

    class Meta:
        model = Fixture
        fields = ('name', 'slug', 'description',
                  'country', 'season', 'image',
                  'start_date', 'type', 'link_blank', 'is_hot', 'channels')

        widgets = {
            'country': forms.widgets.Select(
                attrs={'class': 'form-control custom-select2',
                       'style': 'width: 100%;'}),
            'season': forms.widgets.Select(
                attrs={'class': 'form-control custom-select2',
                       'style': 'width: 100%;'}),
            'channels': forms.widgets.SelectMultiple(
                attrs={'class': 'form-control',
                       'style': 'width: 100%; height: 320px;',
                       'multiple': "multiple"}),
            'type': forms.widgets.Select(
                attrs={'class': 'form-control custom-select2',
                       'style': 'width: 100%;'}),
            'is_hot': forms.widgets.CheckboxInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        team_home = cleaned_data.get("team_home")
        team_away = cleaned_data.get("team_away")

        if team_home and team_away and team_home == team_away:
            msg = "You can't choose team home like team away"
            self.add_error('team_away', msg)


class CreateFixtureView(AdminBaseView, AdminRequiredMixin, CreateView):
    template_name = 'admin/fixtures/create.html'
    model = Fixture
    initial = {
        'country': '189',
        'season': '1',
    }
    form_class = FixtureForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Create Fixture',
                'sidebar': ['fixture']
            }
        }
        context.update(info)
        return context

    def form_valid(self, form):
        fixture = form.save(commit=False)
        fixture.team_home = Team.objects.get(id=form.cleaned_data['team_home'])
        fixture.team_away = Team.objects.get(id=form.cleaned_data['team_away'])
        fixture.tournament = Tournament.objects.get(id=form.cleaned_data['tournament'])
        fixture.save()

        match = Match.objects.create(fixture=fixture)
        match.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('admin:list_fixture')


class UpdateFixtureView(AdminBaseView, AdminRequiredMixin, UpdateView):
    template_name = 'admin/fixtures/update.html'
    model = Fixture
    form_class = FixtureForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Update Fixture',
                'sidebar': ['fixture']
            }
        }
        context.update(info)
        fixture = self.get_object()
        context['form']['team_home'].value = fixture.team_home.id
        context['form']['team_away'].value = fixture.team_away.id
        return context

    def form_valid(self, form):
        fixture = form.save(commit=False)
        fixture.team_home = Team.objects.get(id=form.cleaned_data['team_home'])
        fixture.team_away = Team.objects.get(id=form.cleaned_data['team_away'])
        fixture.tournament = Tournament.objects.get(id=form.cleaned_data['tournament'])
        fixture.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('admin:list_fixture')


class DeleteFixtureView(AdminBaseView, AdminRequiredMixin, DeleteView):
    model = Fixture

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:list_fixture')


class DeleteMultipleFixtureView(AdminBaseView, AdminRequiredMixin, FormView):
    def post(self, request, *args, **kwargs):
        try:
            list = request.POST.get('list', None)
            if list:
                arr = list.split(',')
                Fixture.objects.filter(id__in=arr).delete()
            return HttpResponse(True)
        except:
            return HttpResponse(False)
