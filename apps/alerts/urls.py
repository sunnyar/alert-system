from django.conf.urls import url, include
from .views import (
	AlertListView,
	AlertSearchView
	)

urlpatterns = [
	url(r'^$', AlertListView.as_view(), name="alert-list"),
	url(r'^search/$', AlertSearchView.as_view(), name="alert-search"),
	url(r'^log/search/$', AlertListView.as_view(), name="log-search"),
	url(r'^log/search-box/$', AlertListView.as_view(), name="log-search-box")
]