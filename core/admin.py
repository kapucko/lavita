from django.contrib import admin

from .models import Food

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    pass
admin.site.register(Food, FoodAdmin)
