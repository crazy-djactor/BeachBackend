from rest_framework import serializers

from api.models import ZoneCamera, Beach


class ZoneCameraSerializer(serializers.ModelSerializer):
    beach_name = serializers.SerializerMethodField()

    def get_beach_name(self, obj):
        return obj.beach.beach_name

    class Meta:
        model = ZoneCamera
        fields = ('id', 'count', 'light_state', 'last_updated', 'position', 'beach_name', 'cam_name')
        read_only_fields = ('ip',)


class BeachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beach
        fields = '__all__'

