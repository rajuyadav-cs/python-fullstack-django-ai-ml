from django.contrib import admin
from .models import CharInfo


@admin.register(CharInfo)
class CharInfoAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'gender',
        'element',
        'weapon_type',
        'region',
        'dob',
        'created_at',
    )

    list_filter = (
        'element',
        'gender',
        'weapon_type',
        'region',
    )

    search_fields = (
        'name',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    ordering = (
        'name',
    )

    list_per_page = 20

    fieldsets = (
        (
            'Character Information',
            {
                'fields': (
                    'name',
                    'gender',
                    'element',
                    'weapon_type',
                    'region',
                    'dob',
                    'image',
                )
            },
        ),
        (
            'System Information',
            {
                'fields': (
                    'created_at',
                    'updated_at',
                )
            },
        ),
    )