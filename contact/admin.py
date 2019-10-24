from django.contrib import admin
from .models import Quote, Turns, Model_Quote

# Register your models here.
class TurnsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class QuoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class ModelQAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Turns, TurnsAdmin) 
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Model_Quote, ModelQAdmin)