# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings

from functools import partial


class Alert(models.Model):

	ALERT_STATUS = (
		("Unreviewed", "Unreviewed"),
		("Researching", "Researching"),
		("In Progress", "In Progress"),
		("Resolved", "Resolved"),
	)

	ALERT_SEVERITY = (
		("Low", "LOW"),
		("Medium", "MEDIUM"),
		("High", "HIGH"),
		("Critical", "CRITICAL"),
	)


	client_id = models.CharField(max_length=100, null=True, blank=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	event = models.ManyToManyField("Event", blank=True)
	reviewer = models.CharField(max_length=100, null=True, blank=True)
	review_time = models.DateTimeField(null=True, blank=True)
	status = models.CharField(max_length=20, choices=ALERT_STATUS, default="Unreviewed")
	severity = models.CharField(max_length=10, choices=ALERT_SEVERITY, default="Low")

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('-created_at',)
		db_table = 'Alert'

	def alert_server(self):
		return self.client_id.split('-')[0]

	def alert_user(self):
		return self.client_id.split('-')[1]


class Event(models.Model):

	name = models.CharField(max_length=100, null=True, blank=True)
	created_at = models.DateTimeField(default=partial(timezone.localtime, timezone.now()), 
					null=True)