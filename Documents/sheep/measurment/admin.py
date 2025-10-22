from django.contrib import admin
from .models import Measurment

@admin.register(Measurment)
class MeasurmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'milk')
    search_fields = ('name',)

# Register your models here.
