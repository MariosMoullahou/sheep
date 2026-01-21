from django.contrib import admin
from .models import Sheep

@admin.register(Sheep)
class SheepAdmin(admin.ModelAdmin):
    list_display = ('earing',)
    search_fields = ('earing',)