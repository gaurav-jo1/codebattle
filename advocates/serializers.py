from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Advocate

class AdvocatesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Advocate
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Advocate.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets',]