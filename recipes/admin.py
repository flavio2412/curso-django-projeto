from django.contrib import admin
from .models import Category, Recipe

class CatagoryAdmin(admin.ModelAdmin):
    ...
@admin.register(Recipe)
class Recipeadmin(admin.ModelAdmin):
    ...  
admin.site.register(Category, CatagoryAdmin)
