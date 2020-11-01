from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username',)


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.CustomUser
        fields = "__all__"
