from django.shortcuts import render
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    TemplateView, DetailView, ListView
)
from apps.tournaments.models import Tournament
from apps.fixtures.models import Fixture
from apps.core.views import BaseView
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator


# Create your views here.

class FixtureView(BaseView, TemplateView):
    template_name = 'fixtures/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.now() - timedelta(hours=2)
        info = {
            'info': {
                'title': 'Lịch thi đấu bóng đá',
                'selected': 'all'
            },
            'fixtures': Fixture.objects.filter(type=1).filter(start_date__gt=now).order_by('start_date'),
            'tournaments': Tournament.objects.all()
        }
        context.update(info)
        return context


class FixtureTodayView(BaseView, TemplateView):
    template_name = 'fixtures/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now()
        start_today = datetime(year=today.year, month=today.month, day=today.day, hour=00, minute=00)
        end_today = datetime(year=today.year, month=today.month, day=today.day, hour=23, minute=59)

        now = datetime.now() - timedelta(hours=2)
        info = {
            'info': {
                'title': 'Lịch thi đấu hôm nay',
                'selected': 'today'
            },
            'fixtures': Fixture.objects.filter(type=1).filter(start_date__gt=now).filter(
                start_date__range=[start_today, end_today]).order_by('start_date'),
            'tournaments': Tournament.objects.all()
        }
        context.update(info)
        return context


class FixtureTomorrowView(BaseView, TemplateView):
    template_name = 'fixtures/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now()
        start_today = datetime(year=today.year, month=today.month, day=today.day + 1, hour=00, minute=00)
        end_today = datetime(year=today.year, month=today.month, day=today.day + 1, hour=23, minute=59)
        info = {
            'info': {
                'title': 'Lịch thi đấu ngày mai',
                'selected': 'tomorrow'
            },
            'fixtures': Fixture.objects.filter(type=1).filter(start_date__range=[start_today, end_today]).order_by(
                'start_date'),
            'tournaments': Tournament.objects.all()
        }
        context.update(info)
        return context


class FixtureDetailView(BaseView, DetailView):
    model = Tournament
    template_name = 'fixtures/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.name,
                'selected': self.object.id,
            },
            'fixtures': Fixture.objects.filter(start_date__gt=timezone.now()).filter(tournament=self.object).order_by(
                'start_date'),
            'tournaments': Tournament.objects.all()
        }
        context.update(info)
        return context


class FixtureLiveView(BaseView, DetailView):
    model = Fixture
    template_name = 'fixtures/live.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(FixtureLiveView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.name + ' - Football Online',
            },
            'cur_server': self.current_server()
        }
        context.update(info)
        return context

    def current_server(self):
        cur_server = None
        fixture = self.object
        server = self.request.GET.get('server', None)
        if server:
            if server == '1':
                cur_server = fixture.match.frame_server_1
            elif server == '2':
                cur_server = fixture.match.frame_server_2
            elif server == '3':
                cur_server = fixture.match.frame_server_3
            elif server == '4':
                cur_server = fixture.match.frame_server_4
            elif server == '5':
                cur_server = fixture.match.frame_server_5
            elif server == '6':
                cur_server = fixture.match.frame_server_6
            elif server == '7':
                cur_server = fixture.match.frame_server_7
            elif server == '8':
                cur_server = fixture.match.frame_server_8
            elif server == '9':
                cur_server = fixture.match.frame_1xbet
        else:
            if fixture.match.frame_1xbet:
                cur_server = fixture.match.frame_1xbet
            elif fixture.match.frame_server_1:
                cur_server = fixture.match.frame_server_1
            elif fixture.match.frame_server_2:
                cur_server = fixture.match.frame_server_2
            elif fixture.match.frame_server_3:
                cur_server = fixture.match.frame_server_3
            elif fixture.match.frame_server_4:
                cur_server = fixture.match.frame_server_4
            elif fixture.match.frame_server_5:
                cur_server = fixture.match.frame_server_5
            elif fixture.match.frame_server_6:
                cur_server = fixture.match.frame_server_6
            elif fixture.match.frame_server_7:
                cur_server = fixture.match.frame_server_7
            elif fixture.match.frame_server_8:
                cur_server = fixture.match.frame_server_8

        return cur_server


#########################################################


class FixtureFrameView(BaseView, TemplateView):
    template_name = 'fixtures/frame.html'

    @method_decorator(xframe_options_exempt)
    def dispatch(self, request, *arg, **kwargs):
        return super().dispatch(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.now() - timedelta(hours=2)
        info = {
            'info': {
                'title': 'Lịch thi đấu bóng đá',
                'selected': 'all'
            },
            'fixtures': Fixture.objects.filter(type=1).filter(start_date__gt=now).order_by('start_date'),
            'tournaments': Tournament.objects.all()
        }
        context.update(info)
        return context


class FixtureFrameTodayView(BaseView, TemplateView):
    template_name = 'fixtures/frame.html'

    @method_decorator(xframe_options_exempt)
    def dispatch(self, request, *arg, **kwargs):
        return super().dispatch(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now()
        start_today = datetime(year=today.year, month=today.month, day=today.day, hour=00, minute=00)
        end_today = datetime(year=today.year, month=today.month, day=today.day, hour=23, minute=59)

        now = datetime.now() - timedelta(hours=2)
        info = {
            'info': {
                'title': 'Lịch thi đấu hôm nay',
                'selected': 'today'
            },
            'fixtures': Fixture.objects.filter(type=1).filter(start_date__gt=now).filter(
                start_date__range=[start_today, end_today]).order_by(
                'start_date'),
            'tournaments': Tournament.objects.all()
        }
        context.update(info)
        return context


class FixtureFrameTomorrowView(BaseView, TemplateView):
    template_name = 'fixtures/frame.html'

    @method_decorator(xframe_options_exempt)
    def dispatch(self, request, *arg, **kwargs):
        return super().dispatch(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now()
        start_today = datetime(year=today.year, month=today.month, day=today.day + 1, hour=00, minute=00)
        end_today = datetime(year=today.year, month=today.month, day=today.day + 1, hour=23, minute=59)
        info = {
            'info': {
                'title': 'Lịch thi đấu ngày mai',
                'selected': 'tomorrow'
            },
            'fixtures': Fixture.objects.filter(type=1).filter(start_date__range=[start_today, end_today]).order_by(
                'start_date'),
            'tournaments': Tournament.objects.all()
        }
        context.update(info)
        return context


class FixtureFrameDetailView(BaseView, DetailView):
    model = Tournament
    template_name = 'fixtures/frame.html'

    @method_decorator(xframe_options_exempt)
    def dispatch(self, request, *arg, **kwargs):
        return super().dispatch(request, *arg, **kwargs)

    @method_decorator(cache_page(10 * 60))
    def dispatch(self, request, *arg, **kwargs):
        return super().dispatch(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.name,
                'selected': self.object.id,
            },
            'fixtures': Fixture.objects.filter(start_date__gt=timezone.now()).filter(tournament=self.object).order_by(
                'start_date'),
            'tournaments': Tournament.objects.all()
        }
        context.update(info)
        return context
