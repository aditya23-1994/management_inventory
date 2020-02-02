from django.contrib import admin
from .models import Product, Customer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'quantity', 'is_available')
    search_title = ('name', 'category')

admin.site.register(Product, ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'email','city','state','zipcode')

admin.site.register(Customer,CustomerAdmin)