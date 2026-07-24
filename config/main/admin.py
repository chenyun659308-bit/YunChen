from django.contrib import admin
from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'title', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'phone', 'title', 'content']
    readonly_fields = ['created_at']
    fieldsets = (
        ('留言信息', {'fields': ('name', 'phone', 'email', 'title', 'content')}),
        ('时间信息', {'fields': ('created_at',)}),
    )
