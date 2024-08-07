from django.contrib import admin
from .models import Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    '''
    Admin View for Table
    '''
    list_display = (
        'table_name', 'table_phone', 'table_email',
        'table_capacity', 'table_date', 'table_time'
    )
    list_filter = ('table_capacity', 'table_date', 'table_time')
    search_fields = ('table_name', 'table_phone', 'table_email')
