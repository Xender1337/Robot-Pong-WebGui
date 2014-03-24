from django.contrib import admin
from ping.models import Raspberry

# Register your models here.


class RaspberryAdmin(admin.ModelAdmin):
    list_display=('label', 'status')

admin.site.register(Raspberry, RaspberryAdmin)