from django.contrib import admin

from .models import StaffProfile, TimeOffRequest

admin.site.register(StaffProfile)
admin.site.register(TimeOffRequest)
