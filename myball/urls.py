"""myball URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles import views
from django.contrib.sitemaps.views import sitemap
from apps.fixtures.sitemaps import FixtureSitemap
from apps.posts.sitemaps import PostSitemap

sitemaps = {
    'fixtures': FixtureSitemap(),
    'posts': PostSitemap()
}

urlpatterns = [
    url(r'^', include('apps.homes.urls', namespace='home')),
    url(r'^video/', include('apps.videos.urls', namespace='video')),
    url(r'^tong-hop-ban-thang/', include('apps.clips.urls', namespace='clip')),
    url(r'^giai-tri/', include('apps.relaxs.urls', namespace='relax')),
    url(r'^tin-tuc/', include('apps.posts.urls', namespace='post')),
    url(r'^trang/', include('apps.pages.urls', namespace='page')),
    url(r'^truc-tiep-bong-da/', include('apps.fixtures.urls', namespace='fixture')),
    url(r'^kenh-truyen-hinh/', include('apps.channels.urls', namespace='channel')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', views.static.serve,
        {'document_root': settings.STATIC_ROOT,
         'show_indexes': settings.DEBUG}),
    url(r'^media/(?P<path>.*)$', views.static.serve,
        {'document_root': settings.MEDIA_ROOT,
         'show_indexes': settings.DEBUG}),

    url(r'^admincp/', include('apps.admin.urls', namespace='admin')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^sitemap.xml$', sitemap, {'sitemaps': sitemaps}),
    url(r'^robots.txt$', include('robots.urls')),
]
