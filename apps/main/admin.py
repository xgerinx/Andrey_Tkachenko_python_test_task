from django.contrib import admin
from apps.main.models import Post


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
