from django.shortcuts import get_object_or_404, render

from .models import Recipe


def index(request):
    recipes = Recipe.objects.filter(is_published=True)
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)

def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    context = {
        'recipe': recipe
    }
    return render(request, 'recipe.html', context)
