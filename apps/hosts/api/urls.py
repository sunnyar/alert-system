from django.conf.urls import url
from hosts.api.views import (
	HostListCreateAPIView,
	)

urlpatterns = [
	#url(r'create/(?P<client_id>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/(?P<name>[a-zA-z0-9]+)/$', AlertCreateAPIView.as_view(), name="create"),
    url(r'^$', HostListCreateAPIView.as_view(), name="list-create"),
    # url(r'^(?P<client_id>^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/(?P<name>[a-zA-z0-9]+)/$',
    #     AlertList.as_view())
]