# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings

from functools import partial


class Host(models.Model):


	LOGIN_TYPE = (
		("normal", "normal"),
		("root", "root"),
	)

	server_ip = models.GenericIPAddressField()
	username = models.CharField(max_length=100, null=True, blank=True)
	last_login = models.DateTimeField(auto_now_add=True, null=True)
	login_type = models.CharField(max_length=10, choices=LOGIN_TYPE, default="normal")
	failed_attempts = models.IntegerField(default=0)