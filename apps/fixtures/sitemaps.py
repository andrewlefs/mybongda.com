from django.contrib.sitemaps import Sitemap
from apps.fixtures.models import Fixture 


class FixtureSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Fixture.objects.order_by('-id')
