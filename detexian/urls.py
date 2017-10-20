from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Examples:
    # url(r'^$', 'detexian.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/alerts/', include('alerts.api.urls')),
    url(r'^api-token-auth/', obtain_auth_token),
]