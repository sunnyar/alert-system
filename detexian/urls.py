from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from rest_framework.authtoken.views import obtain_auth_token
from allauth.account.views import password_change
from dashboard.views import DashboardView


urlpatterns = [
    # Examples:
    # url(r'^$', 'detexian.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', DashboardView.as_view(), name="index"),
    url(r'^alerts/', include('alerts.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='account/profile.html'), name="profile"),
    url(r"^accounts/settings/$", password_change,
        name="account_change_password"),
    url(r'^api/host/', include('hosts.api.urls')),
    url(r'^api-token-auth/', obtain_auth_token),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)