from django.shortcuts import get_object_or_404, render

from .models import Recipe


def index(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-created_at')
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

def search(request):
    recipes = []
    if ('search' in request.GET) and request.GET['search']:
        search_key = request.GET['search']
        recipes = (
            Recipe
                .objects
                .filter(is_published=True, name__icontains=search_key)
                .order_by('-created_at')
        )
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)
