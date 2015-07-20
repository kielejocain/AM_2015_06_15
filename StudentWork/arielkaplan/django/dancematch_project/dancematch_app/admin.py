from django.contrib import admin
from models import Dancer, Dance, Schedule, Location, DancePrefs

admin.site.register(Dancer)
admin.site.register(Dance)
admin.site.register(Schedule)
admin.site.register(Location)
admin.site.register(DancePrefs)