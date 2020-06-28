from django.contrib import admin

# Register your models here.
from api.models import Beach, ZoneCamera

admin.site.register(Beach)
admin.site.register(ZoneCamera)