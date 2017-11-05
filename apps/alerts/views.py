# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic.edit import FormView
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from .models import Alert
from .forms import SearchForm
from .search import alert_search

import datetime, calendar
from datetime import timedelta, date, datetime


class AlertListView(LoginRequiredMixin, ListView):

	model = Alert
	template_name = 'alerts/list.html'

	def get_context_data(self, **kwargs):

		today = datetime.now()
		previous_30_days = today - timedelta(days=30)

		context = super(AlertListView, self).get_context_data(**kwargs)
		context['last_30_days_alerts_count'] = Alert.objects.filter(created_at__gte=previous_30_days).count()
		context['today_alerts_count'] = Alert.objects.filter(created_at__date=today.date()).count()
		context['most_20_recent_alerts'] = Alert.objects.all()[:21]

		return context


class AlertSearchView(FormView):
	form_class = SearchForm
	success_url = "/alerts/search/"
	template_name = "alerts/search.html"
	data = {}

	def post(self, request, **kwargs):
		search_text = self.request.POST.get("search_text")
		if self.request.POST and self.request.is_ajax():
			data = {}
			data["alert_list"] = alert_search(str(search_text))
    		return JsonResponse(data)

		return super(AlertSearchView, self).post(request, **kwargs)