from rest_framework import serializers

from api.models import ZoneCamera


class ZoneCameraSerializer(serializers.ModelSerializer):

    class Meta:
        model = ZoneCamera
        fields = ('count', 'light_state', 'last_updated')
        read_only_fields = ('cam_name', 'ip', 'position', 'beach')
