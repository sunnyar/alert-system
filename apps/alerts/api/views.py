from django.http import HttpResponse

from rest_framework.generics import (
	ListCreateAPIView,
	CreateAPIView
	)
from rest_framework.response import Response

from alerts.models import Alert
from .serializers import (
	AlertCreateSerializer,
	AlertListSerializer
	)

class AlertListCreateAPIView(ListCreateAPIView):
	queryset = Alert.objects.all()
	# serializer_class = AlertListCreateSerializer

	http_method_names = [u'get', u'post']

	def get_serializer_class(self):
		if self.request.method == 'POST':
			self.serializer_class = AlertCreateSerializer
		elif self.request.method == 'GET':
			self.serializer_class = AlertListSerializer
		return self.serializer_class