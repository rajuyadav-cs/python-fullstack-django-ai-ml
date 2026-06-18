from django.contrib import admin
from .models import Teams

@admin.register(Teams)
class TeamsAdminModel(admin.ModelAdmin):
    list_display = (
        'team_name',
        'created_by',
        'created_at',
    )