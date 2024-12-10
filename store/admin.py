from django.contrib import admin

from .models import Category,Product



# Register your models here

# class SubCategoryInline(admin.TabularInline):
#     model = SubCategory
#     list_display = ['name']
#     extra = 0

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','description']
    prepopulated_fields = {'slug': ('name',)}

    # inlines = [SubCategoryInline]

admin.site.register(Category,CategoryAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price',
                    'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}

