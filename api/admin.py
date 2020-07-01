from django.contrib import admin

# Register your models here.
from api.models import Beach, Zone, CountLogData, Station, Router, Jetson, Camera

admin.site.register(Beach)
admin.site.register(Zone)
admin.site.register(CountLogData)
admin.site.register(Station)
admin.site.register(Router)
admin.site.register(Jetson)
admin.site.register(Camera)
