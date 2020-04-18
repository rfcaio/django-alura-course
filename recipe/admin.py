from django.contrib import admin

from .models import Recipe

class RecipeList(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('category',)
    list_per_page = 5
    search_fields = ('name',)

admin.site.register(Recipe, RecipeList)
