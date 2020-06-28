from django.db import models


class Beach(models.Model):
    beach_name = models.CharField(max_length=255, unique=True)
    position = models.TextField(max_length=255, null=True)


# Create your models here.
class ZoneCamera(models.Model):
    cam_name = models.CharField(max_length=255, unique=True)
    ip = models.GenericIPAddressField()
    position = models.TextField(max_length=255, null=True)
    beach = models.ForeignKey(Beach, on_delete=models.DO_NOTHING, related_name='zon_cam')
    count = models.IntegerField(null=True)
    light_state = models.IntegerField(null=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True)


class CountLogData(models.Model):
    camera = models.ForeignKey(ZoneCamera, on_delete=models.DO_NOTHING, related_name='count_data')
    date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(null=True)
