# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class AlertsConfig(AppConfig):
	name = 'alerts'

	def ready(self):
		import alerts.signals
