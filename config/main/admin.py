from django.contrib import admin
from django.utils.html import format_html
from .models import Contract, Product

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


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview', 'name', 'name_en', 'category', 'active', 'sort_order', 'updated_at']
    list_display_links = ['id', 'image_preview', 'name']
    list_editable = ['active', 'sort_order']
    list_filter = ['category', 'active']
    search_fields = ['name', 'name_en', 'category', 'desc', 'desc_en']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('基本信息', {
            'fields': (
                'name', 'name_en', 'category', 'desc', 'desc_en', 'active', 'sort_order'
            )
        }),
        ('图片', {
            'fields': ('image', 'legacy_image'),
            'description': '上传新图片后优先使用；也可填写服务器上的图片路径。'
        }),
        ('规格', {
            'fields': ('specs', 'specs_en'),
            'classes': ('wide',)
        }),
        ('时间', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    @admin.display(description='图片')
    def image_preview(self, obj):
        url = obj.image_url
        if not url:
            return '-'
        return format_html('<img src="{}" style="max-height:48px;max-width:80px;object-fit:contain;">', url)
