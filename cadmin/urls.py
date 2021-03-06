from django.conf.urls import url, include
from cadmin import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as password_reset


urlpatterns = [
    url(r'^activate/account/$', views.activate_account, name='activate'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^password-change-done/$', auth_views.password_change_done, {'template_name': 'cadmin/password_change_done.html'}, name='password_change_done'),
    url(r'^password-change/$', auth_views.password_change, {'template_name': 'cadmin/password_change.html','post_change_redirect': 'password_change_done'}, name='password_change'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^login/$', auth_views.login, {'template_name': 'cadmin/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'cadmin/logout.html'}, name='logout'),
    url(r'^post/add/$', views.post_add, name='post_add'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^post/update/(?P<pk>[\d]+)/$', views.post_update, name='post_update'),
    url(r'^post/delete/(?P<pk>[\d]+)/$', views.post_delete, name='post_delete'),
    url(r'^category/$',views.category_list, name='category_list'),
    url(r'^category/add/$', views.category_add, name='category_add'),
    url(r'^category/update/(?P<pk>[\d]+)/$', views.category_update, name='category_update'),
    url(r'^category/delete/(?P<pk>[\d]+)/$', views.category_delete, name='category_delete'),
    url(r'^tag/$', views.tag_list, name="tag_list"),
    url(r'^tag/add/$', views.tag_add, name='tag_add'),
    url(r'^tag/update/(?P<pk>[\d]+)/$', views.tag_update, name='tag_update'),
    url(r'^tag/delete/(?P<pk>[\d]+)/$', views.tag_delete, name='tag_delete'),
    url(r'^account-info/$', views.account_info, name='account_info'),
    
]
