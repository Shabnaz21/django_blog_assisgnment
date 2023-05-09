from django.contrib import admin
from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display =('title', 'slug', 'category', 'post_status',)
    list_filter =('category',)
admin.site.register(Blog,PostAdmin)
admin.site.register(Category)
admin.site.register(Author)
