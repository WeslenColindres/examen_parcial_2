from rest_framework import serializers
from .models import Procurador

class ProcuradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procurador
        fields = '__all__'

