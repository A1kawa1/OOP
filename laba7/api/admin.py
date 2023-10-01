from django.contrib import admin
from api.models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('token',)
