from .models import *
from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class LostAutoSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(slug_field="name", read_only=True)
    model = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = LostAuto
        fields = "__all__"


class LostAutoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostAuto
        fields = ["user", "number", "vin_code", "color"]
