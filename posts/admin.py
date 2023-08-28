from django.contrib import admin
from .models import Post, Comment, Like
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource


admin.site.register(Post, PostAdmin)
