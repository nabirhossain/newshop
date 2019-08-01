from django.contrib import admin
from shop.models import Category, Product

# Register your models here.
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'parent',

    ]
    list_display_links = ['id']
    # list_editable = ['category']
    # list_filter = [
    #     'category',
    # ]
    # search_fields = ['category']
    list_per_page = 30

    class Meta:
        model = Category

class ProductModelAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'id',
        'publish',
        'slider',
        'name',
        'price',
        'quantity',
        'discount',
        'number_of_sales',
        'number_of_views',
        'added',
        'updated'
    ]
    list_display_links = ['__str__']
    list_editable = ['name', 'price']
    list_filter = [
        'publish',
        'slider',
        'category',
        'quantity',
        'discount',
        'number_of_sales',
        'number_of_views',

    ]
    search_fields = ['name', 'description', 'price', 'discount']
    list_per_page = 30

    class Meta:
        model = Product

admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Product, ProductModelAdmin)