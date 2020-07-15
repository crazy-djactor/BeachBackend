from rest_framework import serializers
import json
from api.models import Zone, Beach


class ZoneCameraSerializer(serializers.ModelSerializer):
    beach_name = serializers.SerializerMethodField()
    location_coord = serializers.SerializerMethodField()

    def get_beach_name(self, obj):
        return obj.beach.beach_name

    def get_location_coord(self, obj):
        if obj.location_coord is None:
            return {}
        return json.loads(obj.location_coord)

    def get_location_degree(self, obj):
        if obj.location_degree is None:
            return {}
        return json.loads(obj.location_degree)

    class Meta:
        model = Zone
        fields = ('id', 'count', 'light_state', 'last_updated', 'location_coord', 'location_degree',
                  'beach_name', 'zone_name')
        read_only_fields = ('ip',)


class BeachSerializer(serializers.ModelSerializer):
    location_coord = serializers.SerializerMethodField()
    location_degree = serializers.SerializerMethodField()
    traffic_level = serializers.SerializerMethodField()

    def get_location_coord(self, obj):
        if obj.location_coord is None:
            return {}
        return json.loads(obj.location_coord)

    def get_location_degree(self, obj):
        if obj.location_degree is None:
            return {}
        return json.loads(obj.location_degree)

    def get_traffic_level(self, obj):
        if obj.traffic_level is None:
            return {}
        traffic_level = json.loads(obj.traffic_level)
        return traffic_level

    class Meta:
        model = Beach
        fields = '__all__'

