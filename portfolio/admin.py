from django.contrib import admin
from .models import Projects
# Register your models here.

@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ['title', 'created_at', 'updated_at']
