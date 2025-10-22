from django.contrib import admin
from .models import Sheep  # your custom model

@admin.register(Sheep)
class SheepAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)