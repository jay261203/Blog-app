from django.contrib import admin
# Register your models here.
from .models import Post
from import_export.admin import ImportExportModelAdmin

class postdata(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(Post, postdata)