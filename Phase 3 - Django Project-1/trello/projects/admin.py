from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "project_name",
        "team",
        "created_by",
        "status",
        "start_date",
        "deadline",
    )

    list_filter = (
        "status",
        "team",
        "created_at",
    )

    search_fields = (
        "project_name",
        "description",
    )