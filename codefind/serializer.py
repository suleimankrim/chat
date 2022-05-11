from rest_framework import serializers
from .models import CodeModel


class CodeSerializer(serializers.ModelSerializer):
    number = serializers.CharField(label="code", help_text="Enter SMS Verification")

    class Meta:
        model = CodeModel
        fields = ['number']
