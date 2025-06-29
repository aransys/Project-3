from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'completed', 'due_date', 'created_at']
    list_filter = ['completed', 'due_date']
    search_fields = ['title', 'description']
