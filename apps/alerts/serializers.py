from .models import Alert
from rest_framework import serializers
 
 
class AlertSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Alert
        fields = ('id', 'client_id', 'name', 'event', 'reviewer', 'review_time',
        					'status', 'severity', 'created_at')