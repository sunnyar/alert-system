from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token

from dashboard.views import DashboardView
from alerts.views import AlertListView


urlpatterns = [
    # Examples:
    # url(r'^$', 'detexian.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', DashboardView.as_view(), name="index"),
    url(r'^alerts/$', AlertListView.as_view(), name="alert-list"),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/host/', include('hosts.api.urls')),
    url(r'^api-token-auth/', obtain_auth_token),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)