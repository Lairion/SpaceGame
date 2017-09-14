from django.contrib import admin
from .models import Ship,Character,Engine,Engine_ship,Laser,Laser_ship
# import .models
# Register your models here.
admin.site.register(Character)
admin.site.register(Engine)
admin.site.register(Engine_ship)
admin.site.register(Laser)
admin.site.register(Laser_ship)
admin.site.register(Ship)
