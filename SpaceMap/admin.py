from django.contrib import admin
from .models import StarSystem,Planet,City
# Register your models here.
admin.site.register(StarSystem)
admin.site.register(Planet)
admin.site.register(City)