from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token

from alerts.views import IndexView


urlpatterns = [
    # Examples:
    # url(r'^$', 'detexian.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/alerts/', include('alerts.api.urls')),
    url(r'^api-token-auth/', obtain_auth_token),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)