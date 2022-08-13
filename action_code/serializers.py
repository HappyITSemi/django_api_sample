# coding: utf-8
from rest_framework import serializers
from action_code.models import ActionCode


class ActionCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionCode
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
