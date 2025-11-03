from rest_framework import serializers
from .models import Milk

class MilkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milk
        fields = '__all__'
