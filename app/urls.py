from django.conf.urls import url, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [

url(r'^$', views.home, name='home'),
url(r'^dashboard/', views.dashboard, name='dashboard'),
url(r'^viewer/', views.viewer, name='viewer'),
url(r'^scenes/(?P<id>\d+)/$', views.scenes, name='scenes'),
url(r'^panorama/', views.panorama, name='panorama'),
url(r'^tour/', views.tour, name='tour'),
url(r'^view/(?P<key_id>[0-9a-f-]+)/$', views.view, name='view'),

url(r'^login/$', auth_views.login, name='login'),

url(r'^signup/$', views.signup, name='signup'),
url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),

url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
