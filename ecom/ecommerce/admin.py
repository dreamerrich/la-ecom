from django.contrib import admin
from .models import product,cart
# Register your models here.

admin.site.register(cart)
class productAdmin(admin.ModelAdmin):
    fields = ['product_name','category','prize','image']

admin.site.register(product, productAdmin)
