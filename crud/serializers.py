from rest_framework import serializers
from .models import News,Address

class NewsSerializer(serializers.ModelSerializer):
    class meta:
        model=News
        fields='__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'