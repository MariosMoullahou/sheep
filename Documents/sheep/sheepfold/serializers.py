from rest_framework import serializers
from .models import Milk,Sheep

class MilkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milk
        fields = '__all__'

class CreateSheep(serializers.ModelSerializer):
    class Meta:
        model = Sheep 
        fieds = '__all__'

class SheepData(serializers.ModelSerializer):
    class Meta:
        model = Sheep
        fields = '__all__'