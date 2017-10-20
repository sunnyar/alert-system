from alerts.models import Alert
from rest_framework.serializers import ModelSerializer
 

class AlertCreateSerializer(ModelSerializer): 
    class Meta:
        model = Alert
        fields = ('client_id', 'name')


class AlertListSerializer(ModelSerializer): 
    class Meta:
        model = Alert
        fields = ('id', 'client_id', 'name', 'created_at')