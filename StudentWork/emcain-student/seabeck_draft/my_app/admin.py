from django.contrib import admin

from .models import *

admin.site.register(Registrant)
admin.site.register(Camper)
admin.site.register(Rate)
admin.site.register(Attendance)
admin.site.register(Shirt)
admin.site.register(ShirtOrder)
admin.site.register(FoodPreference)

