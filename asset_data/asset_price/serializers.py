from rest_framework import serializers

class GoldPriceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    updatedAt = serializers.DateTimeField()
    price = serializers.DecimalField(max_digits=20, decimal_places=6)
    symbol = serializers.CharField(max_length=10)
    updatedAtReadable = serializers.CharField(max_length=100)

class AssetPriceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    updatedAt = serializers.DateTimeField()
    price = serializers.DecimalField(max_digits=20, decimal_places=6)
    symbol = serializers.CharField(max_length=10)
    updatedAtReadable = serializers.CharField(max_length=100)