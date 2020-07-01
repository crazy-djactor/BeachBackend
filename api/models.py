from django.db import models


class Beach(models.Model):
    beach_name = models.CharField(max_length=255, unique=True)
    location_coord = models.TextField(max_length=255, null=True, default='{}')
    location_degree = models.TextField(max_length=255, null=True, default='{}')
    traffic_level = models.TextField(max_length=255, null=True)


class Zone(models.Model):
    beach = models.ForeignKey(Beach, on_delete=models.DO_NOTHING, related_name='zon_cam')
    zone_name = models.CharField(max_length=255, unique=True)
    location_coord = models.TextField(max_length=255, null=True, default='{}')
    location_degree = models.TextField(max_length=255, null=True, default='{}')
    count = models.IntegerField(null=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True)
    traffic_level = models.TextField(max_length=255, null=True, default='{}')
    light_state = models.IntegerField(null=True)


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

