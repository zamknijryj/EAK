from django.contrib import admin
from django.db import models
from .models import Post
from pagedown.widgets import AdminPagedownWidget


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['author', 'publish', 'status']
    search_fields = ['body', 'title']
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Post, PostAdmin)
