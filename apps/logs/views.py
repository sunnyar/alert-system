# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

from alerts.forms import SearchForm


class LogSearchView(FormView):
    form_class = SearchForm
    success_url = "/"
    template_name = "logs/search.html"

    def form_valid(self, form):
        print(self.request.POST['id_name'])
        return super(LogSearchView, self).form_valid(form)