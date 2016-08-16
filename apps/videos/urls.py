from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.VideoListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.VideoDetailView.as_view(), name='detail'),
]
