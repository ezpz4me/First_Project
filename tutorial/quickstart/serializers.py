from enum import unique
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import signup

class signupserializer(serializers.ModelSerializer):
    emailid=serializers.EmailField(max_length=256)
    password=serializers.CharField(max_length=50)

    class Meta:
        model=signup
        fields=('__all__')

