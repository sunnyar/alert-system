# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q

from alerts.models import Alert, Event
from hosts.models import Host

import datetime, calendar
from datetime import timedelta, date, datetime


class DashboardView(LoginRequiredMixin, ListView):

	model = Event
	template_name = 'index.html'


	def get_context_data(self, **kwargs):

		previous_30_days = datetime.now() - timedelta(days=30)
 
		last_hour = datetime.now() - timedelta(hours=1)
		this_week = datetime.now() - timedelta(days=7)
		this_month = datetime.now().month

		context = super(DashboardView, self).get_context_data(**kwargs)
		context['hourly_events'] = Event.objects.filter(created_at__gte=last_hour).count()
		context['weekly_events'] = Event.objects.filter(created_at__gte=this_week).count()
		context['monthly_events'] = Event.objects.filter(created_at__month=this_month).count()

		# query = self.request.GET.get('q')
		# if query:
		# 	context["alert_list"] = list(Alert.objects.filter(Q(name__iconatins=query)|
		# 		Q(client_id__icontains=q)))
		# else:
		context["alert_list"] = list(Alert.objects.all())
		context['last_30_days_alerts_count'] = Alert.objects.filter(created_at__gte=previous_30_days).count()
		context['today_alerts_count'] = Alert.objects.filter(created_at__date=datetime.now().date()).count()

		context['host_list'] = Host.objects.values('server_ip').distinct()

		return context