from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.RelaxListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.RelaxDetailView.as_view(), name='detail'),
]
