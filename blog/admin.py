# from django.contrib import admin
from material.admin.options import MaterialModelAdmin
from material.admin.sites import site

from .models import Post, Category

# Register your models here.
class CategoryAdmin(MaterialModelAdmin):
    readonly_fields = ('created', 'updated')
    icon_name = 'book'

class PostAdmin(MaterialModelAdmin):
    readonly_fields = ('created','updated','views')
    icon_name = 'chrome_reader_mode'

site.register(Category, CategoryAdmin)
site.register(Post, PostAdmin)
