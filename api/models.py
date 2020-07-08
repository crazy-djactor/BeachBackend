import json

from django.db import models


class Beach(models.Model):
    beach_name = models.CharField(max_length=255, unique=True)
    location_coord = models.TextField(max_length=255, null=True, default='{}')
    location_degree = models.TextField(max_length=255, null=True, default='{}')
    count = models.IntegerField(null=True)
    light_state = models.IntegerField(null=True)
    traffic_level = models.TextField(max_length=255, null=True)

    def update_state(self):
        try:
            zone_cams = Zone.objects.filter(beach_id=self.id)
            count = 0
            for zone_cam in zone_cams:
                count = count + zone_cam.count

            traffic_level = json.loads(self.traffic_level)
            if 'high' in traffic_level.keys() and 'medium' in traffic_level.keys() and 'low' in traffic_level.keys():
                if count > traffic_level['high']:
                    light_state = 3
                elif count > traffic_level['medium']:
                    light_state = 2
                elif count > traffic_level['low']:
                    light_state = 1
                else:
                    light_state = 0
                return count, light_state
            return 0, 0
        except:
            return 0, 0


class Zone(models.Model):
    beach = models.ForeignKey(Beach, on_delete=models.DO_NOTHING, related_name='zon_cam')
    zone_name = models.CharField(max_length=255, unique=True)
    location_coord = models.TextField(max_length=255, null=True, default='{}')
    location_degree = models.TextField(max_length=255, null=True, default='{}')
    count = models.IntegerField(null=True)
    last_updated = models.DateTimeField(null=True)
    traffic_level = models.TextField(max_length=255, null=True, default='{}')
    light_state = models.IntegerField(null=True)

    def get_light(self, count):
        traffic_level = json.loads(self.traffic_level)
        if 'high' in traffic_level.keys() and 'medium' in traffic_level.keys() and 'low' in traffic_level.keys():
            if count > traffic_level['high']:
                light_state = 3
            elif count > traffic_level['medium']:
                light_state = 2
            elif count > traffic_level['low']:
                light_state = 1
            else:
                light_state = 0
            return light_state
        return 0


class CountLogData(models.Model):
    camera = models.ForeignKey(Zone, on_delete=models.DO_NOTHING, related_name='count_data')
    date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(null=True)


class Station(models.Model):
    beach = models.ForeignKey(Beach, on_delete=models.DO_NOTHING, related_name='station')
    station_id = models.CharField(max_length=255, unique=True)


class Router(models.Model):
    beach = models.ForeignKey(Beach, on_delete=models.DO_NOTHING, related_name='router')
    router_id = models.CharField(max_length=255, null=True)
    ip = models.GenericIPAddressField()
    usr = models.CharField(max_length=255, null=True)
    pwd = models.CharField(max_length=255, null=True)


class Jetson(models.Model):
    beach = models.ForeignKey(Beach, on_delete=models.DO_NOTHING, related_name='jetson')
    jetson_id = models.CharField(max_length=255, null=True)
    ip = models.GenericIPAddressField()
    usr = models.CharField(max_length=255, null=True)
    pwd = models.CharField(max_length=255, null=True)


class Camera(models.Model):
    beach = models.ForeignKey(Beach, on_delete=models.DO_NOTHING, related_name='camera')
    cam_id = models.CharField(max_length=255, null=True)
    ip = models.GenericIPAddressField()
    usr = models.CharField(max_length=255, null=True)
    pwd = models.CharField(max_length=255, null=True)

