from material.admin.options import MaterialModelAdmin
from material.admin.sites import site
from .models import Quote, Turns, Model_Quote

# Register your models here.
class TurnsAdmin(MaterialModelAdmin):
    readonly_fields = ('created', 'updated')

class QuoteAdmin(MaterialModelAdmin):
    readonly_fields = ('created','updated')

class ModelQAdmin(MaterialModelAdmin):
    readonly_fields = ('created','updated')

site.register(Turns, TurnsAdmin) 
site.register(Quote, QuoteAdmin)
site.register(Model_Quote, ModelQAdmin)