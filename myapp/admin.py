from django.contrib import admin
from .models import Dataset, Image

class ImageInline(admin.TabularInline):
    model = Image

class DatasetAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Dataset, DatasetAdmin)