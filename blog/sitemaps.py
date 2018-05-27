from django.conf.urls import url
from blog import views
from django.contrib.flatpages import views as flat_views
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from .models import Post

class StaticSitemap(Sitemap):
	priority = 0.8
	changefreq = 'weekly'
	
	def get_urls(self, site=None, **kwargs):
        site = Site(domain='autoelectronicselectra.com', name='autoelectronicselectra.com')
        return super(BlogSitemap, self).get_urls(site=site, **kwargs)

	# The below method returns all urls defined in urls.py file
	def items(self):
		return ['home_page', 'contact_usg', 'contact_usv', 'services', 'gps_page','cctv_page', 'security_page','feedback',]

	def location(self, item):
         return reverse(items)


class PostSitemap(Sitemap):    
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
