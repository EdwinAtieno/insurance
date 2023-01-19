from typing import Any

from django.contrib import admin

from app.models import (Product, Insurance, Customer)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('id', 'product_name', 'product_price', 'product_description')
    list_filter = ('product_name', 'product_price', 'product_description')
    search_fields = ('product_name', 'product_price', 'product_description')



admin.site.register(Product, ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ('id', 'first_name', 'phone_number', 'kin_first_name', 'kin_id_number')
    search_fields = ('first_name', 'phone_number', 'kin_first_name', 'kin_id_number')
    list_filter = ('first_name', 'phone_number', 'kin_first_name', 'kin_id_number')

admin.site.register(Customer, CustomerAdmin)

class InsuranceAdmin(admin.ModelAdmin):
    model = Insurance
    list_display = ('id', 'product_issued', 'customer')
    search_fields = ('product_issued', 'customer')
    list_filter = ('product_issued', 'customer')

admin.site.register(Insurance, InsuranceAdmin)