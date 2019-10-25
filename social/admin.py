from material.admin.options import MaterialModelAdmin
from material.admin.sites import site
from .models import Link

# Register your models here.
class LinkAdmin(MaterialModelAdmin):
    readonly_fields = ('created','updated')
    icon_name = 'share'

site.register(Link, LinkAdmin)