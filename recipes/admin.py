from django.contrib import admin
from .models import Category, Recipe


# you can to add a model in admin with a function or decorator

class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
