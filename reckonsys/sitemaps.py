# sitemaps.py
from django.contrib.sitemaps import Sitemap
from home.models import HomePage, AboutusPage

class HomePageSitemap(Sitemap):
    def items(self):
        return HomePage.objects.live().public()

    def lastmod(self, obj):
        return obj.latest_revision_created_at

    def changefreq(self, obj):
        return 'weekly'

    def priority(self, obj):
        return 0.5

class AboutusPageSitemap(Sitemap):
    def items(self):
        return AboutusPage.objects.live().public()

    def lastmod(self, obj):
        return obj.latest_revision_created_at

    def changefreq(self, obj):
        return 'daily'

    def priority(self, obj):
        return 0.8
