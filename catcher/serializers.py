from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.Serializer):
    name = serializers.DecimalField(max_digits=5, decimal_places=2)

    def create(self, validated_data):
        return Message.objects.create(**validated_data)