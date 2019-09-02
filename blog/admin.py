from django.contrib import admin
from .models import Contact, Order
# Register your models here.


class OrderDisplay(admin.ModelAdmin):
    list_display = ('name', 'phone', 'checker')


admin.site.register(Contact)
admin.site.register(Order, OrderDisplay)
