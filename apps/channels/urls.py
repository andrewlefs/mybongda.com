from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<fixture>[0-9]+)/(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.ChannelDetailView.as_view(), name='detail'),
    url(r'^nhung/(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.ChannelFrameDetailView.as_view(), name='frame'),
]
