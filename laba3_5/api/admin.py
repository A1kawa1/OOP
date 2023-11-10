from django.contrib import admin

from api.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'completed')
