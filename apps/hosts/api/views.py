from django.http import HttpResponse

from rest_framework.generics import (
	ListCreateAPIView,
	CreateAPIView
	)
from rest_framework.response import Response

from hosts.models import Host
from alerts.models import Alert
from .serializers import (
	HostCreateSerializer,
	HostListSerializer
	)

class HostListCreateAPIView(ListCreateAPIView):
	queryset = Host.objects.all()

	http_method_names = [u'get', u'post']

	def get_serializer_class(self):
		if self.request.method == 'POST':
			self.serializer_class = HostCreateSerializer
		elif self.request.method == 'GET':
			self.serializer_class = HostListSerializer
		return self.serializer_class

	def create(self, request, *args, **kwargs):
		print "Request :", request.data

		if request.data:
			server_ip = request.data["server_ip"]
			username  = request.data["username"]

			name = ""
			if Host.objects.filter(server_ip=server_ip, username=username).exists():
				if request.data["login_type"] == "root":
					name = "ROOT LOGIN"
			else:
				if request.data["login_type"] == "root":
					name = "ROOT FIRST LOGIN"
				else:
					name = "FIRST LOGIN"

			if name and int(request.data["failed_attempts"]) >= 10:
				name = "BRUTEFORCE " + name

			if name:
				Alert.objects.create(
					client_id = "%s-%s" % (server_ip, username),
					name = name
				)

		return super(HostListCreateAPIView, self).create(request, *args, **kwargs)
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)