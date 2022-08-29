from rest_framework import serializers
from bikeapi.models import Bikes


class BikeSerializers(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    colour=serializers.CharField()
    cc=serializers.IntegerField()
    brand=serializers.CharField()
    price=serializers.IntegerField()


class BikeModelserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Bikes
        fields="__all__"