from django.contrib import admin

from .models import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'count',
    )
    search_fields = (
        'text',
    )
    ordering = (
        '-count',
    )
