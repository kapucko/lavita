from django.contrib import admin

from .models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "category_display_name", "weight", "price")


admin.site.register(Food, FoodAdmin)
admin.site.site_header = admin.site.site_title = "Lavita administration"