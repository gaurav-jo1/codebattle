from dataclasses import field, fields
from statistics import mode
from rest_framework import serializers
from .models import Advocates

class AdvocatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocates
        fields = '__all__'