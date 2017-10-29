from hosts.models import Host
from rest_framework.serializers import ModelSerializer
 

class HostCreateSerializer(ModelSerializer): 
    class Meta:
        model = Host
        fields = ('server_ip', 'username', 'login_type', 'failed_attempts')


class HostListSerializer(ModelSerializer): 
    class Meta:
        model = Host
        fields = ('server_ip', 'username', 'last_login', 'login_type', 'failed_attempts')