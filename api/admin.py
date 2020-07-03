from django.contrib import admin

# Register your models here.
from api.models import Beach, Zone, CountLogData, Station, Router, Jetson, Camera


class BeachAdmin(admin.ModelAdmin):
    list_display = ['beach_name', 'count', 'light_state', 'traffic_level', 'location_coord']


class ZoneAdmin(admin.ModelAdmin):
    list_display = ['zone_name', 'count', 'light_state', 'traffic_level', 'last_updated']


admin.site.register(Beach, BeachAdmin)
admin.site.register(Zone, ZoneAdmin)
admin.site.register(CountLogData)
admin.site.register(Station)
admin.site.register(Router)
admin.site.register(Jetson)
admin.site.register(Camera)
