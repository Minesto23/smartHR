from material.admin.options import MaterialModelAdmin
from material.admin.sites import site
from .models import WorkTeam, Who_We_Are

# Register your models here.
class WorkTeamAdmin(MaterialModelAdmin):
    readonly_fields = ('created','updated')

class Who_We_AreAdmin(MaterialModelAdmin):
    readonly_fields = ('created','updated')

site.register(WorkTeam, WorkTeamAdmin)
site.register(Who_We_Are, Who_We_AreAdmin)