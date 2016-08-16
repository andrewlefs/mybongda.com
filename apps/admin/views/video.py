from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView
)
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django import forms
from datetime import datetime
from apps.core.views import AdminRequiredMixin, AdminBaseView
from apps.videos.models import Video
from apps.teams.models import Team
from apps.categories.models import Category


class ListVideoView(AdminBaseView, AdminRequiredMixin, ListView):
    template_name = 'admin/videos/list.html'
    model = Video
    paginate_by = settings.NUM_IN_PAGE

    def get_queryset(self):
        return Video.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'List Video',
                'sidebar': ['video']
            }
        }
        context.update(info)
        return context


class VideoForm(forms.ModelForm):
    """docstring for VideoForm"""
    category = forms.ModelChoiceField(queryset=Category.objects.filter(type=2).order_by('-id'),
                                      widget=forms.Select(attrs={'class': 'form-control select2',
                                                                 'style': 'width: 100%;'}))
    team_home = forms.IntegerField()
    team_away = forms.IntegerField()

    class Meta:
        model = Video
        fields = ('name', 'slug', 'description',
                  'score', 'tournament', 'image',
                  'frame', 'category')

        widgets = {
            'tournament': forms.widgets.Select(
                attrs={'class': 'form-control custom-select2',
                       'style': 'width: 100%;'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        team_home = cleaned_data.get("team_home")
        team_away = cleaned_data.get("team_away")

        if team_home and team_away and team_home == team_away:
            msg = "You can't choose team home like team away"
            self.add_error('team_away', msg)


class CreateVideoView(AdminBaseView, AdminRequiredMixin, CreateView):
    template_name = 'admin/videos/create.html'
    model = Video
    initial = {
        'tournament': '1',
        'category': '1',
    }
    form_class = VideoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Create Video',
                'sidebar': ['video']
            }
        }
        context.update(info)
        return context

    def form_valid(self, form):
        video = form.save(commit=False)
        video.team_home = Team.objects.get(id=form.cleaned_data['team_home'])
        video.team_away = Team.objects.get(id=form.cleaned_data['team_away'])
        video.match_date = datetime.today()
        video.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('admin:list_video')


class UpdateVideoView(AdminBaseView, AdminRequiredMixin, UpdateView):
    template_name = 'admin/videos/update.html'
    model = Video
    form_class = VideoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Update Video',
                'sidebar': ['video']
            }
        }
        context.update(info)
        video = self.get_object()
        context['form']['team_home'].value = video.team_home.id
        context['form']['team_away'].value = video.team_away.id
        return context

    def form_valid(self, form):
        video = form.save(commit=False)
        video.team_home = Team.objects.get(id=form.cleaned_data['team_home'])
        video.team_away = Team.objects.get(id=form.cleaned_data['team_away'])
        video.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('admin:list_video')


class DeleteVideoView(AdminBaseView, AdminRequiredMixin, DeleteView):
    model = Video

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:list_video')
