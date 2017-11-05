# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.http import JsonResponse, HttpResponse

from alerts.forms import SearchForm
from alerts.search import event_search

class LogSearchView(FormView):
	form_class = SearchForm
	success_url = "/logs/search/"
	template_name = "logs/search.html"
	data = {}

	def post(self, request, **kwargs):
		search_text = self.request.POST.get("search_text")
		if self.request.POST and self.request.is_ajax():
			data = {}
			data["log_list"] = event_search(str(search_text))
    		return JsonResponse(data)

		return super(LogSearchView, self).post(request, **kwargs)