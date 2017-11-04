from django.conf.urls import url, include
from .views import (
	LogSearchView
	)

urlpatterns = [
	url(r'^search/$', LogSearchView.as_view(), name="log-search"),
	url(r'^search-box/$', LogSearchView.as_view(), name="log-search-box")
]