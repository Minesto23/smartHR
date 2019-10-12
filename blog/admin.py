from django.contrib import admin
from .models import Post, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
