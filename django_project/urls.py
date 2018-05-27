"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from blog import views
from django.contrib.flatpages import views as flat_views
from django.contrib.sitemaps import views as sitemaps_views
from django.views.decorators.cache import cache_page
from blog.sitemaps import *

# Dictionary containing your sitemap classes
sitemaps = {
   'static': StaticSitemap,
}

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
	url(r'^sitemap.xml/', sitemaps_views.sitemap,{'sitemaps': sitemaps}, name='sitemaps'),
    url(r'', include('blog.urls')),                         
    url(r'^', include('flatpages_i18n.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^cadmin/', include('cadmin.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
