from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.PageDetailView.as_view(), name='detail'),
]
