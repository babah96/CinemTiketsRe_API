from rest_framework import serializers
from tikets.models import Guest,Movie,Reservation


class MovieSerializer(serializers.ModelSerializer):
    class meta:
        model = Movie
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class meta:
        model = Reservation
        fields = '__all__'


class GeustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['pk', 'reservation', 'name', 'mobile']
