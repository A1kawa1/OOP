from django.contrib import admin
from goods.models import Good


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'price')
