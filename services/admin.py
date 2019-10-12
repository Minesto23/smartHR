from django.contrib import admin
from .models import Service, Our_Services

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class Our_ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Service, ServiceAdmin)
admin.site.register(Our_Services, Our_ServiceAdmin)