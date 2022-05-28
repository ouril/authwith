from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import MyModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MyModelSer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'

