from django.shortcuts import render


def index(request):
    recipes = [
        {
            'description': 'Cheese pizza'
        },
        {
            'description': 'Chocolate cake'
        }
    ]
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)
