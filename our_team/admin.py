from django.contrib import admin
from .models import WorkTeam, Who_We_Are

# Register your models here.
class WorkTeamAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class Who_We_AreAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(WorkTeam, WorkTeamAdmin)
admin.site.register(Who_We_Are, Who_We_AreAdmin)