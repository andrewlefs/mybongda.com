from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ClipListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.ClipDetailView.as_view(), name='detail'),
]
