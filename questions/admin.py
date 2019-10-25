from material.admin.options import MaterialModelAdmin
from material.admin.sites import site
from .models import Question
# Register your models here.

class QuestionAdmin(MaterialModelAdmin):
    readonly_fields = ('created','updated')
    icon_name = 'reorder'


site.register(Question, QuestionAdmin)
