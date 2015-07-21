from django.contrib import admin
from models import (Dancer, Dance, Schedule, Location, DancePrefs,
                    SkillLevel, Activity, Goals, DanceRole)

admin.site.register(Dancer)
admin.site.register(Dance)
admin.site.register(Schedule)
admin.site.register(Location)
admin.site.register(DancePrefs)
admin.site.register(SkillLevel)
admin.site.register(Activity)
admin.site.register(Goals)
admin.site.register(DanceRole)