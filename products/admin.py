from django.contrib import admin
from .models import Product, Category, Sub_category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'tittle')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_category)