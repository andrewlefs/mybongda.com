from datetime import datetime
from datetime import timedelta
from django.utils import timezone
from django.views.generic import (
    TemplateView
)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from apps.posts.models import Post
from apps.videos.models import Video
from apps.clips.models import Clip
from apps.fixtures.models import Fixture
from apps.relaxs.models import Relax
from apps.core.views import BaseView


# Create your views here.

class HomePageView(BaseView, TemplateView):
    template_name = 'homes/index.html'

    @method_decorator(cache_page(30))
    def dispatch(self, request, *arg, **kwargs):
        return super().dispatch(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        now = datetime.now() - timedelta(hours=2)
        info = {
            'info': {
                'title': 'Trực Tiếp Bóng Đá - Xem Bóng Đá Trực Tuyến'
            },
            'post_top': Post.objects.order_by('-id')[0:10],
            'post_analytic': Post.objects.filter(category__id=3).order_by('-id')[0:9],
            'post_news': Post.objects.filter(category__id=8).order_by('-id')[0:5],
            'post_wags': Post.objects.filter(category__name='Wags').order_by('-id')[0:5],
            # 'videos_highlight': Video.objects.filter(category__name='Highlight').order_by('-id')[0:6],
            'videos_highlight': Clip.objects.order_by('-id')[0:12],

            'fixtures_main': Fixture.objects.filter(type=1).filter(start_date__gt=now).order_by(
                'start_date')[:10],
            'fixtures_extra': Fixture.objects.filter(type=2).filter(start_date__gt=now).order_by(
                'start_date'),
            'relaxs': Relax.objects.order_by('-id')[0:6]
        }
        context.update(info)
        return context
