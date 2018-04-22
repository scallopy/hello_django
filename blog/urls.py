from django.conf.urls import url
from . import views
from django.contrib.flatpages import views as flat_views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    url(r'^sitemap\.xml/$', sitemap, {'sitemaps' : sitemaps} , name='sitemap'),
    url(r'^contact/usg/$', views.contact_usg, name='contact_usg'),
    url(r'^contact/usv/$', views.contact_usv, name='contact_usv'),
    url(r'^accounts/profile/$', views.admin_page, name='admin_page'),
    url(r'^about/$', flat_views.flatpage, {'url': '/about/'}, name='about'),
    url(r'^about/us/$', flat_views.flatpage, {'url': '/about/us/'}, name='about_us'),
    url(r'^login/$', views.login, name='blog_login'),
    url(r'^logout/$', views.logout, name='blog_logout'),
    url(r'^admin_page/$', views.admin_page, name='admin_page'),
    url(r'^lousy-login/$', views.lousy_login, name='lousy_login'),
    url(r'^lousy-secret/$', views.lousy_secret, name='lousy_secret'),
    url(r'^lousy-logout/$', views.lousy_logout, name='lousy_logout'),
    url(r'^save_session_data/$', views.save_session_data, name='save_session_data'),
    url(r'^access_session_data/$', views.access_session_data, name='access_session_data'),
    url(r'^delete_session_data/$', views.delete_session_data, name='delete_session_data'),
    url(r'^test_delete/$', views.test_delete, name='test_delete'),
    url(r'^test_session/$', views.test_session, name='test_session'),
    url(r'^stop-tracking/$', views.stop_tracking, name='stop_tracking'),
    url(r'^track_user/$', views.track_user, name='track_user'),
    url(r'^cookie/$', views.test_cookie, name='cookie'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^blog/$', views.test_redirect, name='test_redirect'),
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.post_by_category, name='post_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_by_tag, name='post_by_tag'),
    url(r'^(?P<pk>\d+)/(?P<post_slug>[\w\d-]+)$', views.post_detail, name='post_detail'),
    url(r'^$', views.home_page, name='home_page'),
    url(r'^post/list/$',views.post_list, name='post_list'),
    url(r'^opening/$', views.opening_hours, name='opening_hours'),
    ]
    
