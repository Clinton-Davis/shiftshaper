from django.contrib import admin
from .models import Roster, Location, Shift

admin.site.register(Roster)
admin.site.register(Shift)
admin.site.register(Location)
