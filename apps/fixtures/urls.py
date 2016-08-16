from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.FixtureView.as_view(), name='index'),
    url(r'^hom-nay/$', views.FixtureTodayView.as_view(), name='today'),
    url(r'^ngay-mai$', views.FixtureTomorrowView.as_view(), name='tomorrow'),
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.FixtureDetailView.as_view(), name='detail'),
    url(r'^truc-tuyen/(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.FixtureLiveView.as_view(), name='live'),

    url(r'^nhung/$', views.FixtureFrameView.as_view(), name='frame'),
    url(r'^nhung/hom-nay/$', views.FixtureFrameTodayView.as_view(), name='frame_today'),
    url(r'^nhung/ngay-mai$', views.FixtureFrameTomorrowView.as_view(), name='frame_tomorrow'),
    url(r'^nhung/(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.FixtureFrameDetailView.as_view(), name='frame_detail'),
]


