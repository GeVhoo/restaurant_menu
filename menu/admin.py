from django.contrib import admin

from .models import Category, Allergen, Dish


admin.site.register(Category)
admin.site.register(Allergen)
admin.site.register(Dish)
