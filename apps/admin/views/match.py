from django.views.generic import (
    UpdateView, DeleteView
)
from django.core.urlresolvers import reverse_lazy
from django import forms
from apps.core import utils
from apps.core.views import AdminRequiredMixin, AdminBaseView
from apps.fixtures.models import FrameAuto
from apps.matches.models import Match
import traceback


class MatchForm(forms.ModelForm):
    """docstring for MatchForm"""

    class Meta:
        model = Match
        fields = (
            'link_statistics', 'link_now_goal', 'link_betradar',
            'link_odds', 'link_sopcast', 'frame_server_1',
            'frame_server_2', 'frame_server_3', 'frame_server_4',
            'frame_server_5', 'frame_server_6', 'frame_server_7',
            'frame_server_8', 'frame_1xbet',
        )


class UpdateMatchView(AdminBaseView, AdminRequiredMixin, UpdateView):
    template_name = 'admin/matches/update.html'
    model = Match
    form_class = MatchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Update Match',
                'sidebar': ['fixture']
            }
        }
        context['fixture'] = self.object.fixture
        context.update(info)
        return context

    def form_valid(self, form):
        match = form.save()

        try:
            if utils.check_if_auto(match.frame_1xbet):
                data = utils.get_xbet_line(match.frame_1xbet)
                if data and data['type'] == 'line':
                    match.frame_1xbet = data['url']
                    match.save()
                    if not FrameAuto.objects.filter(url=data['url']):
                        FrameAuto.objects.create(url=data['url'])
                elif data and data['type'] == 'live':
                    match.frame_1xbet = data['url']
                    match.save()
                    if not FrameAuto.objects.filter(url=data['url']):
                        FrameAuto.objects.create(url=data['url'], frame=data['frame'])
                    else:
                        frame_temp = FrameAuto.objects.get(url=data['url'])
                        frame_temp.frame = data['frame']

            if match.frame_server_1 and utils.check_if_auto(match.frame_server_1):
                get_data = FrameAuto.objects.filter(url=match.frame_server_1)
                if not get_data:
                    FrameAuto.objects.create(url=match.frame_server_1)
            elif match.frame_server_2 and utils.check_if_auto(match.frame_server_2):
                get_data = FrameAuto.objects.filter(url=match.frame_server_2)
                if not get_data:
                    FrameAuto.objects.create(url=match.frame_server_2)
            elif match.frame_server_3 and utils.check_if_auto(match.frame_server_3):
                get_data = FrameAuto.objects.filter(url=match.frame_server_3)
                if not get_data:
                    FrameAuto.objects.create(url=match.frame_server_3)
            elif match.frame_server_4 and utils.check_if_auto(match.frame_server_4):
                get_data = FrameAuto.objects.filter(url=match.frame_server_4)
                if not get_data:
                    FrameAuto.objects.create(url=match.frame_server_4)
            elif match.frame_server_5 and utils.check_if_auto(match.frame_server_5):
                get_data = FrameAuto.objects.filter(url=match.frame_server_5)
                if not get_data:
                    FrameAuto.objects.create(url=match.frame_server_5)
            elif match.frame_server_6 and utils.check_if_auto(match.frame_server_6):
                get_data = FrameAuto.objects.filter(url=match.frame_server_6)
                if not get_data:
                    FrameAuto.objects.create(url=match.frame_server_6)
            elif match.frame_server_7 and utils.check_if_auto(match.frame_server_7):
                get_data = FrameAuto.objects.filter(url=match.frame_server_7)
                if not get_data:
                    FrameAuto.objects.create(url=match.frame_server_7)
            elif match.frame_server_8 and utils.check_if_auto(match.frame_server_8):
                get_data = FrameAuto.objects.filter(url=match.frame_server_8)
                if not get_data:
                    FrameAuto.objects.create(url=match.frame_server_8)
        except:
            print(traceback.format_exc())

        return super(UpdateMatchView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('admin:list_fixture')


class DeleteMatchView(AdminBaseView, AdminRequiredMixin, DeleteView):
    model = Match

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:list_fixture')
