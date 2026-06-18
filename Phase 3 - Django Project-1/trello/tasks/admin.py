from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "project",
        "assigned_to",
        "status",
        "priority",
        "deadline",
    )

    list_filter = (
        "status",
        "priority",
        "deadline",
    )

    search_fields = (
        "title",
        "description",
    )