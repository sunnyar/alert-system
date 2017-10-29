# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Alert

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
