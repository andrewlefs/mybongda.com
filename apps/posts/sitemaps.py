from django.contrib.sitemaps import Sitemap
from apps.posts.models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.order_by('-id')
