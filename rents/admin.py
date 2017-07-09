from django.contrib import admin

from .models import Product, Customer, Rent, RentDetail

admin.site.register(Product)
admin.site.register(Customer)

class RentDetailInline(admin.TabularInline):
    model = RentDetail

class RentAdmin(admin.ModelAdmin):
    inlines = [
        RentDetailInline
    ]

admin.site.register(Rent, RentAdmin)