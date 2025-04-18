from django.contrib import admin

# Register your models here.
from visits.models import Visit

@admin.register(Visit)
class VisitsAdmin(admin.ModelAdmin):
    # What to show
    list_display = ['__str__', 'page', 'username', 'timestamp']
    list_filter = ['page', 'username', 'timestamp']
    search_fields = ['page', 'username']
    # Timestamp is readonly by default
    readonly_fields = ['timestamp']
